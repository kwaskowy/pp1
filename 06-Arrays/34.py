array1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
array2=[5,2,3,8,19,20]
wynik=None
if (all(x in array1 for x in array2)):
    wynik= True
if wynik==True:
    print(f"Zbiór {array2} jest podzbiorem {array1}")
else: print(f"Zbiór {array2} nie jest podzbiorem {array1}")