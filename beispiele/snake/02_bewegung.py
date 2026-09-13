"""Etappe 2: Automatische Bewegung; an der Wand bleibt der Kopf stehen."""
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18
TEMPO = 8


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    pygame.display.set_caption("Snake – Bewegung mit Pfeiltasten")
    uhr = pygame.time.Clock()
    x, y = 5, 8
    dx, dy = 1, 0
    laeuft = True

    while laeuft:
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False
                elif ereignis.key == pygame.K_UP:
                    dx, dy = 0, -1
                elif ereignis.key == pygame.K_DOWN:
                    dx, dy = 0, 1
                elif ereignis.key == pygame.K_LEFT:
                    dx, dy = -1, 0
                elif ereignis.key == pygame.K_RIGHT:
                    dx, dy = 1, 0

        neu_x = x + dx
        neu_y = y + dy
        # Erst prüfen, dann bewegen. Randfelder sind noch gültig.
        if 0 <= neu_x < SPALTEN and 0 <= neu_y < ZEILEN:
            x, y = neu_x, neu_y

        fenster.fill((20, 25, 35))
        pygame.draw.rect(fenster, (80, 220, 120), (x * ZELLE, y * ZELLE, ZELLE, ZELLE))
        pygame.display.flip()
        # Ein Feld pro Bild: höchstens acht Schritte pro Sekunde.
        uhr.tick(TEMPO)

    pygame.quit()


if __name__ == "__main__":
    main()
