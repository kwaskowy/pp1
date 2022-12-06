array=[4,5,12,172,43,15,1,3,54,2,24,51,2,41,21,21,45,142,192,42,1,23,5,32,63]
parzyste=[]
nieparzyste=[]
for x in array:
    if x%2==0:
        parzyste.append(x)
    else:  nieparzyste.append(x)
wynik=parzyste+nieparzyste
print(wynik)