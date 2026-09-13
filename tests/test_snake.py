"""Rule tests and headless event/render smoke tests for the teaching stages."""
import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import patch

os.environ["SDL_VIDEODRIVER"] = "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

ROOT = Path(__file__).resolve().parents[1]


def load(filename):
    spec = importlib.util.spec_from_file_location("lesson_" + filename[:2], ROOT / "beispiele/snake" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


game = load("03_snake.py")


class SnakeRules(unittest.TestCase):
    def test_initial_state_and_restart(self):
        snake, direction, food, points, status = game.neue_runde()
        self.assertEqual((len(snake), direction, points, status), (3, (1, 0), 0, "spiel"))
        self.assertNotIn(food, snake)
        snake.append((2, 8))
        self.assertEqual(len(game.neue_runde()[0]), 3)

    def test_movement_keeps_length(self):
        snake = [(5, 8), (4, 8), (3, 8)]
        result, food, points, status = game.schritt(snake, (1, 0), (10, 10), 0)
        self.assertEqual(result, [(6, 8), (5, 8), (4, 8)])
        self.assertEqual((points, status), (0, "spiel"))
        self.assertEqual(snake, [(5, 8), (4, 8), (3, 8)])

    def test_food_grows_and_scores(self):
        snake, food, points, status = game.schritt([(5, 8), (4, 8), (3, 8)], (1, 0), (6, 8), 0)
        self.assertEqual((len(snake), points, status), (4, 1, "spiel"))
        self.assertNotIn(food, snake)

    def test_four_walls(self):
        for head, direction in [((0, 5), (-1, 0)), ((23, 5), (1, 0)), ((5, 0), (0, -1)), ((5, 17), (0, 1))]:
            with self.subTest(head=head):
                self.assertEqual(game.schritt([head], direction, (10, 10), 0)[3], "verloren")

    def test_body_collision(self):
        snake = [(2, 2), (2, 3), (1, 3), (1, 2), (1, 1)]
        self.assertEqual(game.schritt(snake, (-1, 0), (10, 10), 0)[3], "verloren")

    def test_vacated_tail_is_allowed(self):
        snake = [(2, 2), (2, 3), (1, 3), (1, 2)]
        self.assertEqual(game.schritt(snake, (-1, 0), (10, 10), 0)[3], "spiel")

    def test_reverse_rejected(self):
        self.assertEqual(game.waehle_richtung((1, 0), (-1, 0)), (1, 0))
        self.assertEqual(game.waehle_richtung((1, 0), (0, -1)), (0, -1))

    def test_last_free_cell_and_win(self):
        with patch.object(game, "SPALTEN", 2), patch.object(game, "ZEILEN", 2):
            snake = [(0, 0), (0, 1), (1, 1)]
            self.assertEqual(game.neues_futter(snake), (1, 0))
            result, food, points, status = game.schritt(snake, (1, 0), (1, 0), 7)
            self.assertEqual((len(result), food, points, status), (4, None, 8, "gewonnen"))
            self.assertIsNone(game.neues_futter(result))


class SnakeWindow(unittest.TestCase):
    def run_frames(self, module, frames):
        with patch.object(pygame.event, "get", side_effect=frames), patch.object(pygame.time, "Clock"):
            module.main()
        self.assertFalse(pygame.get_init())

    def test_all_stages_draw_and_close(self):
        for filename in ["01_spielfenster.py", "02_bewegung.py", "03_snake.py"]:
            for closing in [pygame.event.Event(pygame.QUIT), pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)]:
                with self.subTest(filename=filename, closing=closing):
                    self.run_frames(load(filename), [[], [closing]])

    def test_only_one_turn_per_step(self):
        up = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        left = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        with patch.object(game, "schritt", wraps=game.schritt) as step:
            self.run_frames(game, [[up, left], [pygame.event.Event(pygame.QUIT)]])
        self.assertEqual(step.call_args.args[1], (0, -1))

    def test_gameover_and_r_restart(self):
        restart = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)
        with patch.object(game, "neue_runde", wraps=game.neue_runde) as reset:
            self.run_frames(game, [[] for _ in range(20)] + [[restart], [pygame.event.Event(pygame.QUIT)]])
        self.assertEqual(reset.call_count, 2)


if __name__ == "__main__":
    unittest.main()
