print("=== MONSTERKAMPF ===")

spieler_leben = 100
monster_leben = 30

def angreifen(schaden):
    return schaden

print("Monster:", monster_leben, "HP")

schaden = angreifen(10)
monster_leben = monster_leben - schaden

print("Du verursachst", schaden, "Schaden.")
print("Monster:", monster_leben, "HP")
