tekst = "You never get a second chance to make a first impression"
def calculations(t):
    litery = 0
    for x in t:
        if x == "e":
            litery += 1
    print("Liczba liter e w tekście:",litery)
calculations(tekst)
