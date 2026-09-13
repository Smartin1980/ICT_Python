"""Einfaches Snake: Pfeiltasten, Futter, Punkte, Kollision und Neustart."""
import random
import pygame

ZELLE = 25
SPALTEN = 24
ZEILEN = 18
TEMPO = 8


def neues_futter(schlange):
    freie_felder = []
    for y in range(ZEILEN):
        for x in range(SPALTEN):
            if (x, y) not in schlange:
                freie_felder.append((x, y))
    if not freie_felder:
        return None  # Alle Felder belegt: gewonnen!
    return random.choice(freie_felder)


def neue_runde():
    schlange = [(5, 8), (4, 8), (3, 8)]
    richtung = (1, 0)
    return schlange, richtung, neues_futter(schlange), 0, "spiel"


def waehle_richtung(richtung, wunsch):
    # Eine direkte Umkehr würde den Kopf in den eigenen Hals bewegen.
    if wunsch == (-richtung[0], -richtung[1]):
        return richtung
    return wunsch


def schritt(schlange, richtung, futter, punkte):
    kopf_x, kopf_y = schlange[0]
    dx, dy = richtung
    kopf = (kopf_x + dx, kopf_y + dy)
    x, y = kopf
    if not (0 <= x < SPALTEN and 0 <= y < ZEILEN):
        return schlange, futter, punkte, "verloren"

    frisst = kopf == futter
    # Ohne Futter verschwindet die Schwanzspitze im selben Schritt.
    koerper = schlange if frisst else schlange[:-1]
    if kopf in koerper:
        return schlange, futter, punkte, "verloren"

    schlange = [kopf] + schlange
    if frisst:
        punkte = punkte + 1
        futter = neues_futter(schlange)
    else:
        schlange.pop()

    if futter is None:
        return schlange, futter, punkte, "gewonnen"
    return schlange, futter, punkte, "spiel"


def main():
    pygame.init()
    fenster = pygame.display.set_mode((SPALTEN * ZELLE, ZEILEN * ZELLE))
    schrift = pygame.font.Font(None, 32)
    uhr = pygame.time.Clock()
    schlange, richtung, futter, punkte, status = neue_runde()
    laeuft = True

    while laeuft:
        # Höchstens eine Richtungsänderung zwischen zwei Schritten zulassen.
        gedreht = False
        for ereignis in pygame.event.get():
            if ereignis.type == pygame.QUIT:
                laeuft = False
            elif ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_ESCAPE:
                    laeuft = False
                elif ereignis.key == pygame.K_r and status != "spiel":
                    schlange, richtung, futter, punkte, status = neue_runde()
                    gedreht = True
                elif status == "spiel" and not gedreht:
                    wunsch = richtung
                    if ereignis.key == pygame.K_UP:
                        wunsch = (0, -1)
                    elif ereignis.key == pygame.K_DOWN:
                        wunsch = (0, 1)
                    elif ereignis.key == pygame.K_LEFT:
                        wunsch = (-1, 0)
                    elif ereignis.key == pygame.K_RIGHT:
                        wunsch = (1, 0)
                    neue_richtung = waehle_richtung(richtung, wunsch)
                    if neue_richtung != richtung:
                        richtung = neue_richtung
                        gedreht = True

        if not laeuft:
            break
        if status == "spiel":
            schlange, futter, punkte, status = schritt(schlange, richtung, futter, punkte)

        fenster.fill((20, 25, 35))
        if futter is not None:
            x, y = futter
            pygame.draw.rect(fenster, (255, 190, 60), (x * ZELLE, y * ZELLE, ZELLE, ZELLE))
        for x, y in schlange:
            pygame.draw.rect(fenster, (80, 220, 120), (x * ZELLE, y * ZELLE, ZELLE - 1, ZELLE - 1))

        pygame.display.set_caption("Snake | Punkte: " + str(punkte) + " | Pfeiltasten | Esc: Ende")
        if status != "spiel":
            meldung = "Gewonnen!" if status == "gewonnen" else "Game Over!"
            text = schrift.render(meldung + "  R: Neustart", True, (255, 255, 255))
            position = text.get_rect(center=(SPALTEN * ZELLE // 2, ZEILEN * ZELLE // 2))
            pygame.draw.rect(fenster, (20, 25, 35), position.inflate(20, 20))
            fenster.blit(text, position)
        pygame.display.flip()
        uhr.tick(TEMPO)

    pygame.quit()


if __name__ == "__main__":
    main()
