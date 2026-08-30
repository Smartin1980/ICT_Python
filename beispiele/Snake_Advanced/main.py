from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pygame


WIDTH, HEIGHT = 960, 720
CELL = 24
GRID_W, GRID_H = WIDTH // CELL, HEIGHT // CELL
FPS = 60
HIGHSCORE_FILE = Path(__file__).with_name("highscore.json")

BG = (7, 10, 22)
GRID = (21, 35, 60)
WHITE = (235, 244, 255)
MUTED = (135, 153, 178)
GREEN = (70, 255, 165)
GREEN_DARK = (18, 150, 91)
RED = (255, 82, 102)
YELLOW = (255, 213, 92)
CYAN = (67, 211, 255)
PURPLE = (188, 114, 255)
WALL = (79, 92, 121)


DIRECTIONS = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0),
}


MODES = [
    {
        "name": "Classic",
        "subtitle": "Pure Snake mit wachsendem Tempo.",
        "walls": False,
        "portals": False,
    },
    {
        "name": "Maze",
        "subtitle": "Hindernisse und gute Reflexe.",
        "walls": True,
        "portals": False,
    },
    {
        "name": "Portal Rush",
        "subtitle": "Portale, Hindernisse und Chaos.",
        "walls": True,
        "portals": True,
    },
]


@dataclass
class Particle:
    x: float
    y: float
    vx: float
    vy: float
    life: float
    color: tuple[int, int, int]
    radius: float

    def update(self, dt: float) -> bool:
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 80 * dt
        self.life -= dt
        self.radius = max(0, self.radius - 5 * dt)
        return self.life > 0 and self.radius > 0


@dataclass
class PowerUp:
    kind: str
    pos: tuple[int, int]
    ttl: float

    @property
    def color(self) -> tuple[int, int, int]:
        return {"slow": CYAN, "shield": PURPLE, "boost": YELLOW}[self.kind]

    @property
    def label(self) -> str:
        return {"slow": "S", "shield": "H", "boost": "x2"}[self.kind]


class SnakeGame:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Snake Advanced")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font_big = pygame.font.Font(None, 78)
        self.font_mid = pygame.font.Font(None, 38)
        self.font_small = pygame.font.Font(None, 25)
        self.mode_index = 0
        self.highscore = self.load_highscore()
        self.muted = False
        self.state = "menu"
        self.running = True
        self.t = 0.0
        self.reset()

    def load_highscore(self) -> int:
        try:
            data = json.loads(HIGHSCORE_FILE.read_text(encoding="utf-8"))
            return int(data.get("highscore", 0))
        except (FileNotFoundError, ValueError, json.JSONDecodeError):
            return 0

    def save_highscore(self) -> None:
        HIGHSCORE_FILE.write_text(
            json.dumps({"highscore": self.highscore}, indent=2),
            encoding="utf-8",
        )

    def reset(self) -> None:
        start = (GRID_W // 2, GRID_H // 2)
        self.snake = [start, (start[0] - 1, start[1]), (start[0] - 2, start[1])]
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.food = (0, 0)
        self.score = 0
        self.level = 1
        self.move_timer = 0.0
        self.base_delay = 0.14
        self.grow = 0
        self.particles: list[Particle] = []
        self.powerups: list[PowerUp] = []
        self.effects = {"slow": 0.0, "shield": 0.0, "boost": 0.0}
        self.obstacles: set[tuple[int, int]] = set()
        self.portals: list[tuple[int, int]] = []
        self.game_message = ""
        self.build_level()
        self.spawn_food()

    def mode(self) -> dict[str, object]:
        return MODES[self.mode_index]

    def build_level(self) -> None:
        self.obstacles.clear()
        self.portals.clear()

        if self.mode()["walls"]:
            count = min(8 + self.level * 3, 42)
            protected = set(self.snake)
            if hasattr(self, "food"):
                protected.add(self.food)
            if hasattr(self, "powerups"):
                protected.update(power.pos for power in self.powerups)
            protected.update((x, y) for x in range(GRID_W // 2 - 4, GRID_W // 2 + 5)
                             for y in range(GRID_H // 2 - 4, GRID_H // 2 + 5))
            while len(self.obstacles) < count:
                pos = (random.randrange(2, GRID_W - 2), random.randrange(3, GRID_H - 2))
                if pos not in protected:
                    self.obstacles.add(pos)

        if self.mode()["portals"]:
            while len(self.portals) < 2:
                pos = self.random_free_cell()
                if pos not in self.portals:
                    self.portals.append(pos)

    def random_free_cell(self) -> tuple[int, int]:
        blocked = set(self.snake) | self.obstacles | {self.food}
        blocked.update(power.pos for power in self.powerups)
        blocked.update(self.portals)
        while True:
            pos = (random.randrange(1, GRID_W - 1), random.randrange(3, GRID_H - 1))
            if pos not in blocked:
                return pos

    def spawn_food(self) -> None:
        self.food = self.random_free_cell()

    def spawn_powerup(self) -> None:
        if len(self.powerups) >= 2:
            return
        kind = random.choice(["slow", "shield", "boost"])
        self.powerups.append(PowerUp(kind=kind, pos=self.random_free_cell(), ttl=8.5))

    def burst(self, cell: tuple[int, int], color: tuple[int, int, int], amount: int = 18) -> None:
        cx = cell[0] * CELL + CELL / 2
        cy = cell[1] * CELL + CELL / 2
        for _ in range(amount):
            angle = random.random() * math.tau
            speed = random.uniform(80, 270)
            self.particles.append(
                Particle(
                    cx,
                    cy,
                    math.cos(angle) * speed,
                    math.sin(angle) * speed,
                    random.uniform(0.25, 0.75),
                    color,
                    random.uniform(3, 7),
                )
            )

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key(event.key)

    def handle_key(self, key: int) -> None:
        if key == pygame.K_m:
            self.muted = not self.muted
            return

        if self.state == "menu":
            if key in (pygame.K_LEFT, pygame.K_a):
                self.mode_index = (self.mode_index - 1) % len(MODES)
            elif key in (pygame.K_RIGHT, pygame.K_d):
                self.mode_index = (self.mode_index + 1) % len(MODES)
            elif key in (pygame.K_RETURN, pygame.K_SPACE):
                self.reset()
                self.state = "playing"
            elif key == pygame.K_ESCAPE:
                self.running = False
            return

        if key == pygame.K_ESCAPE:
            self.state = "menu"
            return
        if key in (pygame.K_p, pygame.K_SPACE) and self.state in ("playing", "paused"):
            self.state = "paused" if self.state == "playing" else "playing"
            return
        if key == pygame.K_r:
            self.reset()
            self.state = "playing"
            return

        if self.state == "playing" and key in DIRECTIONS:
            nd = DIRECTIONS[key]
            if (nd[0] + self.direction[0], nd[1] + self.direction[1]) != (0, 0):
                self.next_direction = nd

    def update(self, dt: float) -> None:
        self.t += dt
        self.particles = [p for p in self.particles if p.update(dt)]

        if self.state != "playing":
            return

        for key in list(self.effects):
            self.effects[key] = max(0.0, self.effects[key] - dt)

        for power in self.powerups:
            power.ttl -= dt
        self.powerups = [power for power in self.powerups if power.ttl > 0]

        if random.random() < 0.006:
            self.spawn_powerup()

        delay = max(0.055, self.base_delay - (self.level - 1) * 0.008)
        if self.effects["slow"] > 0:
            delay *= 1.75

        self.move_timer += dt
        while self.move_timer >= delay:
            self.move_timer -= delay
            self.step()

    def step(self) -> None:
        self.direction = self.next_direction
        head = self.snake[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

        if self.mode()["portals"] and new_head in self.portals:
            other = self.portals[1] if new_head == self.portals[0] else self.portals[0]
            new_head = other
            self.burst(other, CYAN, 24)

        if self.hit_wall(new_head) or new_head in self.obstacles or new_head in self.snake[:-1]:
            if self.effects["shield"] > 0:
                self.effects["shield"] = 0
                self.burst(head, PURPLE, 30)
                self.direction = (-self.direction[0], -self.direction[1])
                self.next_direction = self.direction
                return
            self.end_game()
            return

        self.snake.insert(0, new_head)

        ate = new_head == self.food
        if ate:
            gained = 20 * (2 if self.effects["boost"] > 0 else 1)
            self.score += gained
            self.grow += 2
            self.burst(self.food, GREEN, 26)
            self.spawn_food()
            if self.score // 120 + 1 > self.level:
                self.level += 1
                self.build_level()
        else:
            for power in list(self.powerups):
                if new_head == power.pos:
                    self.activate_powerup(power)
                    self.powerups.remove(power)
                    break

        if self.grow > 0:
            self.grow -= 1
        else:
            self.snake.pop()

    def hit_wall(self, pos: tuple[int, int]) -> bool:
        return pos[0] < 0 or pos[1] < 2 or pos[0] >= GRID_W or pos[1] >= GRID_H

    def activate_powerup(self, power: PowerUp) -> None:
        durations = {"slow": 5.0, "shield": 7.0, "boost": 6.0}
        self.effects[power.kind] = durations[power.kind]
        self.score += 10
        self.burst(power.pos, power.color, 30)

    def end_game(self) -> None:
        self.state = "gameover"
        self.game_message = "Neuer Highscore!" if self.score > self.highscore else "Game Over"
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.burst(self.snake[0], RED, 55)

    def draw(self) -> None:
        self.screen.fill(BG)
        self.draw_background()
        if self.state == "menu":
            self.draw_menu()
        else:
            self.draw_game()
            if self.state == "paused":
                self.draw_overlay("Pause", "Leertaste: weiter  |  R: Neustart  |  Esc: Menue")
            elif self.state == "gameover":
                self.draw_overlay(self.game_message, "R: nochmal spielen  |  Esc: Menue")
        pygame.display.flip()

    def draw_background(self) -> None:
        for y in range(2, GRID_H):
            yy = y * CELL
            color = tuple(min(255, c + int(10 * math.sin(self.t + y * 0.3))) for c in GRID)
            pygame.draw.line(self.screen, color, (0, yy), (WIDTH, yy), 1)
        for x in range(GRID_W):
            xx = x * CELL
            pygame.draw.line(self.screen, GRID, (xx, CELL * 2), (xx, HEIGHT), 1)

    def draw_menu(self) -> None:
        title = self.font_big.render("Snake Advanced", True, GREEN)
        self.screen.blit(title, title.get_rect(center=(WIDTH // 2, 120)))
        subtitle = self.font_mid.render("Waehle einen Modus und druecke Enter", True, WHITE)
        self.screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 175)))

        for idx, mode in enumerate(MODES):
            rect = pygame.Rect(0, 0, 250, 165)
            rect.center = (WIDTH // 2 + (idx - self.mode_index) * 290, 355)
            selected = idx == self.mode_index
            fill = (18, 29, 50) if selected else (12, 18, 32)
            border = GREEN if selected else GRID
            pygame.draw.rect(self.screen, fill, rect, border_radius=8)
            pygame.draw.rect(self.screen, border, rect, 3 if selected else 1, border_radius=8)
            name = self.font_mid.render(str(mode["name"]), True, GREEN if selected else WHITE)
            self.screen.blit(name, name.get_rect(center=(rect.centerx, rect.y + 48)))
            self.draw_wrapped_text(str(mode["subtitle"]), rect.inflate(-36, -70), MUTED)

        info = self.font_small.render("Pfeile: Modus wechseln  |  M: Ton  |  Esc: Ende", True, MUTED)
        self.screen.blit(info, info.get_rect(center=(WIDTH // 2, 610)))
        hs = self.font_mid.render(f"Highscore: {self.highscore}", True, YELLOW)
        self.screen.blit(hs, hs.get_rect(center=(WIDTH // 2, 660)))

    def draw_game(self) -> None:
        self.draw_hud()
        self.draw_cells(self.obstacles, WALL, 4)
        self.draw_portals()
        self.draw_food()
        for power in self.powerups:
            self.draw_powerup(power)
        self.draw_snake()
        self.draw_particles()

    def draw_hud(self) -> None:
        pygame.draw.rect(self.screen, (10, 16, 31), (0, 0, WIDTH, CELL * 2))
        items = [
            f"Score {self.score}",
            f"Level {self.level}",
            f"Highscore {self.highscore}",
            f"Modus {self.mode()['name']}",
        ]
        x = 18
        for item in items:
            text = self.font_small.render(item, True, WHITE)
            self.screen.blit(text, (x, 15))
            x += text.get_width() + 34
        self.draw_effects()

    def draw_effects(self) -> None:
        x = WIDTH - 265
        for kind, color in [("slow", CYAN), ("shield", PURPLE), ("boost", YELLOW)]:
            if self.effects[kind] > 0:
                label = self.font_small.render(f"{kind.upper()} {self.effects[kind]:.0f}s", True, color)
                self.screen.blit(label, (x, 42))
                x += label.get_width() + 16

    def draw_cells(self, cells: Iterable[tuple[int, int]], color: tuple[int, int, int], inset: int) -> None:
        for cell in cells:
            rect = pygame.Rect(cell[0] * CELL + inset, cell[1] * CELL + inset, CELL - inset * 2, CELL - inset * 2)
            pygame.draw.rect(self.screen, color, rect, border_radius=5)

    def draw_snake(self) -> None:
        for i, cell in enumerate(reversed(self.snake)):
            ratio = i / max(1, len(self.snake) - 1)
            color = blend(GREEN_DARK, GREEN, ratio)
            rect = pygame.Rect(cell[0] * CELL + 2, cell[1] * CELL + 2, CELL - 4, CELL - 4)
            pygame.draw.rect(self.screen, color, rect, border_radius=7)
        head = self.snake[0]
        hx, hy = head[0] * CELL, head[1] * CELL
        glow = pygame.Rect(hx - 2, hy - 2, CELL + 4, CELL + 4)
        pygame.draw.rect(self.screen, GREEN, glow, 2, border_radius=9)

    def draw_food(self) -> None:
        pulse = 4 + math.sin(self.t * 7) * 2
        cx = self.food[0] * CELL + CELL // 2
        cy = self.food[1] * CELL + CELL // 2
        pygame.draw.circle(self.screen, (40, 255, 140), (cx, cy), int(CELL // 2 - 3))
        pygame.draw.circle(self.screen, WHITE, (cx - 3, cy - 3), int(pulse))

    def draw_powerup(self, power: PowerUp) -> None:
        cx = power.pos[0] * CELL + CELL // 2
        cy = power.pos[1] * CELL + CELL // 2
        radius = int(10 + math.sin(self.t * 8) * 2)
        pygame.draw.circle(self.screen, power.color, (cx, cy), radius)
        pygame.draw.circle(self.screen, WHITE, (cx, cy), radius, 1)
        label = self.font_small.render(power.label, True, BG)
        self.screen.blit(label, label.get_rect(center=(cx, cy + 1)))

    def draw_portals(self) -> None:
        for idx, pos in enumerate(self.portals):
            cx = pos[0] * CELL + CELL // 2
            cy = pos[1] * CELL + CELL // 2
            radius = 11 + int(math.sin(self.t * 6 + idx) * 3)
            pygame.draw.circle(self.screen, CYAN, (cx, cy), radius, 3)
            pygame.draw.circle(self.screen, PURPLE, (cx, cy), max(4, radius - 6), 2)

    def draw_particles(self) -> None:
        for p in self.particles:
            alpha_color = tuple(max(0, min(255, c)) for c in p.color)
            pygame.draw.circle(self.screen, alpha_color, (int(p.x), int(p.y)), int(p.radius))

    def draw_overlay(self, title: str, subtitle: str) -> None:
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 145))
        self.screen.blit(overlay, (0, 0))
        title_surf = self.font_big.render(title, True, WHITE)
        self.screen.blit(title_surf, title_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 45)))
        sub_surf = self.font_mid.render(subtitle, True, GREEN)
        self.screen.blit(sub_surf, sub_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25)))

    def draw_wrapped_text(self, text: str, rect: pygame.Rect, color: tuple[int, int, int]) -> None:
        words = text.split()
        lines: list[str] = []
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if self.font_small.size(candidate)[0] <= rect.width:
                line = candidate
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        y = rect.y + 82
        for line in lines:
            surf = self.font_small.render(line, True, color)
            self.screen.blit(surf, surf.get_rect(center=(rect.centerx, y)))
            y += 25

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(FPS) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


if __name__ == "__main__":
    SnakeGame().run()
