def f(array2D):
    wynik= []
    licznik=0
    i=0
    while i<len(array2D[0]):
        wynik.append(0)
        i+=1
    for item in array2D:
        for x in item:
            wynik[licznik]+=x
            licznik+=1
            if licznik==len(array2D[0]):
                licznik=0
    return wynik

                


