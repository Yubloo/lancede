import random

nbde7 = 0
nbdelanc = 0
nbde7pourc = 0

nbdelancplayer = input("Combien voulez vous faire de lancés de 2 dés: ")

while nbdelanc < int(nbdelancplayer):
    de1 = random.randint(0, 6)
    de2 = random.randint(0, 6)
    result = de1 + de2
    nbdelanc += 1
    if result == 7:
        nbde7 += 1
        print("7")
    else:
        print(result)

print("Vérification terminée:\nPour ", nbdelancplayer, " lancé le chiffre 7 resort ", nbde7, " fois")
