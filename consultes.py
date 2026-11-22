from ciutats import ciutats

codi = input("Escriu-lo: ")
trobada = False
for nom, dades in ciutats.items():
    if dades["codi_postal"] == codi:
        print("El codi postal", codi, "correspon a", nom)
        trobada = True
if not trobada:
    print("Codi postal no trobat")
