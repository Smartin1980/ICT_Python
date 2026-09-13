"""Etappe 1: Ein Fenster und ein Schlangenkopf auf einem Raster."""
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    pygame.display.set_caption("Snake – mein erstes Fenster")
    uhr = pygame.time.Clock()
    laeuft = True

    while laeuft:
        # Ereignisse abholen, damit das Fenster auf Eingaben reagiert.
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False

        fenster.fill((20, 25, 35))
        pygame.draw.rect(fenster, (80, 220, 120), (5 * ZELLE, 8 * ZELLE, ZELLE, ZELLE))
        pygame.display.flip()
        uhr.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
