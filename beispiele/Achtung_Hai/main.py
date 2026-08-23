"""Einstiegspunkt fuer Pygame Zero.

Starten mit:
    pgzrun main.py
"""

import achtung_hai as game


WIDTH = game.WIDTH
HEIGHT = game.HEIGHT
TITLE = game.TITLE


def _connect_pgz_globals():
    game.screen = screen
    game.clock = clock


def draw():
    _connect_pgz_globals()
    game.draw()


def on_mouse_down(pos):
    _connect_pgz_globals()
    game.on_mouse_down(pos)


def on_key_down(key, mod, unicode):
    _connect_pgz_globals()
    game.on_key_down(key, mod, unicode)


if __name__ == "__main__":
    import pgzrun

    pgzrun.go()
