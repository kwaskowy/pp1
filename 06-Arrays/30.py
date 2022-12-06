def minmax(array):
    najmniejsza=66666**66666
    największa=0
    wynik=[]
    for x in array:
        if x>największa:
            największa=x
    for x in array:
        if x<najmniejsza:
            najmniejsza=x
    wynik.append(najmniejsza)
    wynik.append(największa)
    return wynik

print(minmax([4,6,12,20,10,9,15]))