"""Achtung, Hai! – animierte Lehrerversion für Pygame Zero.

Starten mit:  pgzrun main.py

Befehle:
    V = ein Feld vorwärts
    R = 90 Grad nach rechts drehen
    L = 90 Grad nach links drehen
"""

import re
from pathlib import Path

import pygame


MODULE_DIR = Path(__file__).resolve().parent

WIDTH = 1180
HEIGHT = 920
TITLE = "Achtung, Hai! – Lösungswege testen"

# Das Originalbild ist 1024 × 1536 Pixel gross. Es wird links verkleinert.
BOARD_X = 20
BOARD_Y = 20
BOARD_W = 580
BOARD_H = 870
SCALE_X = BOARD_W / 1024
SCALE_Y = BOARD_H / 1536

# Rastergrenzen im Originalbild (6 Spalten × 7 Zeilen)
GRID_LEFT = 15
GRID_TOP = 328
CELL_W = (1007 - GRID_LEFT) / 6
CELL_H = (1466 - GRID_TOP) / 7

PANEL_X = 630

WHITE = (248, 250, 252)
INK = (24, 45, 63)
BLUE = (18, 113, 184)
LIGHT_BLUE = (221, 243, 250)
GREEN = (28, 153, 91)
RED = (207, 61, 61)
ORANGE = (238, 154, 45)
GREY = (106, 119, 130)

# Koordinaten: (Zeile, Spalte), Zählung beginnt bei 0.
START = (6, 3)
SHARKS = {(0, 2), (1, 4), (2, 2), (2, 4), (3, 1), (3, 2),
          (4, 1), (4, 4), (6, 0), (6, 1)}
DOCKS = {(0, 1), (1, 1), (0, 5), (1, 5)}
GOALS = {(1, 0): 1, (1, 2): 2, (0, 4): 3, (2, 5): 4}

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # N, O, S, W
DIRECTION_NAMES = ["Norden", "Osten", "Süden", "Westen"]


class InputBox:
    def __init__(self, rect, label, placeholder, allowed=None, max_length=80):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.placeholder = placeholder
        self.allowed = allowed
        self.max_length = max_length
        self.text = ""
        self.active = False

    def click(self, pos):
        self.active = self.rect.collidepoint(pos)

    def key(self, key, unicode_text):
        if not self.active:
            return
        if key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            self.active = False
        elif unicode_text and unicode_text.isprintable() and len(self.text) < self.max_length:
            if self.allowed is None or unicode_text.upper() in self.allowed:
                self.text += unicode_text.upper() if self.allowed else unicode_text

    def draw(self):
        screen.draw.text(self.label, (self.rect.x, self.rect.y - 29),
                         fontsize=25, color=INK)
        colour = BLUE if self.active else GREY
        screen.draw.filled_rect(self.rect, WHITE)
        screen.draw.rect(self.rect, colour)
        shown = self.text if self.text else self.placeholder
        shown_colour = INK if self.text else (145, 153, 160)
        screen.draw.text(shown, (self.rect.x + 12, self.rect.y + 12),
                         fontsize=24, color=shown_colour)


name_box = InputBox((PANEL_X, 170, 510, 52), "Name der Schülerin / des Schülers",
                    "z. B. Mia")
command_box = InputBox((PANEL_X, 270, 510, 52), "Befehlsfolge",
                       "z. B. V V L V", allowed={"V", "R", "L", " ", ",", ";", "-"})

start_button = pygame.Rect(PANEL_X, 350, 245, 58)
reset_button = pygame.Rect(PANEL_X + 265, 350, 245, 58)

row, col = START
direction = 0
commands = []
command_index = 0
running = False
status = "Name und Befehlsfolge eingeben."
status_colour = INK
visited = [START]


def load_board():
    path = MODULE_DIR / "images" / "achtung_hai_2.png"
    image = pygame.image.load(str(path)).convert()
    return pygame.transform.smoothscale(image, (BOARD_W, BOARD_H))


board_surface = None


def reset_game(message="Bereit für eine neue Abfolge."):
    global row, col, direction, commands, command_index, running
    global status, status_colour, visited
    clock.unschedule(execute_next_command)
    row, col = START
    direction = 0
    commands = []
    command_index = 0
    running = False
    visited = [START]
    status = message
    status_colour = INK


def parse_commands(text):
    """Akzeptiert z. B. 'V V R V', 'VVRV' oder 'vor, rechts, vor'."""
    cleaned = text.upper()
    replacements = {
        "VORWÄRTS": "V", "VORWAERTS": "V", "VOR": "V",
        "RECHTS": "R", "LINKS": "L",
    }
    for word, short in replacements.items():
        cleaned = cleaned.replace(word, short)
    return re.findall(r"[VRL]", cleaned)


def start_run():
    global commands, command_index, running, status, status_colour
    reset_game("")
    commands = parse_commands(command_box.text)
    if not name_box.text.strip():
        status = "Bitte zuerst einen Namen eingeben."
        status_colour = RED
        return
    if not commands:
        status = "Bitte mindestens einen Befehl V, R oder L eingeben."
        status_colour = RED
        return
    command_index = 0
    running = True
    status = f"{name_box.text}: Fahrt läuft …"
    status_colour = BLUE
    clock.schedule(execute_next_command, 1.0)


def stop(message, colour):
    global running, status, status_colour
    running = False
    status = message
    status_colour = colour
    clock.unschedule(execute_next_command)


def execute_next_command():
    global row, col, direction, command_index
    if not running:
        return
    if command_index >= len(commands):
        stop("Abfolge beendet – noch kein Steg erreicht.", ORANGE)
        return

    command = commands[command_index]
    command_index += 1

    if command == "R":
        direction = (direction + 1) % 4
    elif command == "L":
        direction = (direction - 1) % 4
    else:
        dr, dc = DIRECTIONS[direction]
        new_position = (row + dr, col + dc)
        if not (0 <= new_position[0] < 7 and 0 <= new_position[1] < 6):
            stop("Stopp: Das Boot würde das Spielfeld verlassen!", RED)
            return
        if new_position in SHARKS:
            row, col = new_position
            visited.append(new_position)
            stop("Achtung, Hai! Die Fahrt ist hier zu Ende.", RED)
            return
        if new_position in DOCKS:
            stop("Stopp: Das Boot kann nicht durch einen Holzsteg fahren.", RED)
            return
        row, col = new_position
        visited.append(new_position)
        if new_position in GOALS:
            number = GOALS[new_position]
            stop(f"Geschafft! {name_box.text} erreicht Steg {number}.", GREEN)
            return

    if command_index >= len(commands):
        stop("Abfolge beendet – noch kein Steg erreicht.", ORANGE)
    else:
        clock.schedule(execute_next_command, 1.0)


def cell_center(position):
    r, c = position
    original_x = GRID_LEFT + (c + 0.5) * CELL_W
    original_y = GRID_TOP + (r + 0.5) * CELL_H
    return (BOARD_X + original_x * SCALE_X,
            BOARD_Y + original_y * SCALE_Y)


def draw_boat(center, heading):
    """Gut sichtbares, drehbares Unterrichtsboot ohne weitere Bilddatei."""
    cx, cy = center
    local = [(0, -37), (25, -18), (22, 30), (0, 40), (-22, 30), (-25, -18)]
    angle = -heading * 90
    points = []
    for x, y in local:
        rotated = pygame.Vector2(x, y).rotate(angle)
        points.append((cx + rotated.x, cy + rotated.y))
    pygame.draw.polygon(screen.surface, (245, 176, 65), points)
    pygame.draw.polygon(screen.surface, (55, 38, 22), points, 4)
    pygame.draw.circle(screen.surface, (255, 240, 115), (int(cx), int(cy)), 9)
    pygame.draw.circle(screen.surface, WHITE, (int(cx), int(cy)), 4)


def draw_button(rect, text, colour, enabled=True):
    fill = colour if enabled else (170, 178, 184)
    screen.draw.filled_rect(rect, fill)
    screen.draw.rect(rect, INK)
    screen.draw.text(text, center=rect.center, fontsize=27, color=WHITE)


def draw_command_strip():
    screen.draw.text("Ausführung", (PANEL_X, 445), fontsize=27, color=INK)
    if not commands:
        screen.draw.text("Noch keine Befehle", (PANEL_X, 485), fontsize=23, color=GREY)
        return
    x, y = PANEL_X, 485
    for index, command in enumerate(commands):
        rect = pygame.Rect(x, y, 43, 43)
        if running and index == command_index:
            colour = ORANGE
        elif index < command_index:
            colour = GREEN
        else:
            colour = LIGHT_BLUE
        screen.draw.filled_rect(rect, colour)
        screen.draw.rect(rect, INK)
        screen.draw.text(command, center=rect.center, fontsize=25, color=INK)
        x += 49
        if x + 43 > WIDTH - 25:
            x = PANEL_X
            y += 49


def draw():
    global board_surface
    screen.fill((238, 246, 249))
    if board_surface is None:
        board_surface = load_board()
    screen.surface.blit(board_surface, (BOARD_X, BOARD_Y))

    # Besuchte Felder markieren und aktuelles Boot darüberzeichnen.
    for pos in visited[:-1]:
        x, y = cell_center(pos)
        pygame.draw.circle(screen.surface, (255, 255, 255), (int(x), int(y)), 9)
        pygame.draw.circle(screen.surface, BLUE, (int(x), int(y)), 9, 3)
    x, y = cell_center((row, col))
    pygame.draw.circle(screen.surface, WHITE, (int(x), int(y)), 48)
    pygame.draw.circle(screen.surface, BLUE, (int(x), int(y)), 48, 5)
    draw_boat((x, y), direction)

    screen.draw.text("ACHTUNG, HAI!", (PANEL_X, 32), fontsize=47,
                     color=INK, bold=True)
    screen.draw.text("Lösungswege gemeinsam testen", (PANEL_X, 88),
                     fontsize=28, color=BLUE)
    name_box.draw()
    command_box.draw()
    draw_button(start_button, "START", GREEN, not running)
    draw_button(reset_button, "ZURÜCKSETZEN", BLUE)
    draw_command_strip()

    screen.draw.text(status, (PANEL_X, 660), width=510, fontsize=29,
                     color=status_colour, bold=True)
    screen.draw.text(f"Position: Zeile {row + 1}, Spalte {col + 1}",
                     (PANEL_X, 745), fontsize=23, color=INK)
    screen.draw.text(f"Blickrichtung: {DIRECTION_NAMES[direction]}",
                     (PANEL_X, 778), fontsize=23, color=INK)
    screen.draw.text("V = vorwärts   R = rechts   L = links",
                     (PANEL_X, 835), fontsize=22, color=GREY)


def on_mouse_down(pos):
    name_box.click(pos)
    command_box.click(pos)
    if start_button.collidepoint(pos) and not running:
        start_run()
    elif reset_button.collidepoint(pos):
        reset_game()


def on_key_down(key, mod, unicode):
    name_box.key(key, unicode)
    command_box.key(key, unicode)
    if key == pygame.K_TAB:
        name_box.active = not name_box.active
        command_box.active = not name_box.active
    elif key in (pygame.K_RETURN, pygame.K_KP_ENTER) and not running:
        start_run()
    elif key == pygame.K_ESCAPE:
        reset_game()


if __name__ == "__main__":
    import pgzrun

    pgzrun.go()
