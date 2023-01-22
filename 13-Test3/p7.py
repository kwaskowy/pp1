class C():
    @staticmethod
    def m1(n):
        array=[]
        wynik=[]
        liczba=""
        n = str(n)
        for x in n:
            array.append(x)
        for x in array:
            if int(x)%2==0:
                wynik.append(x)
        for x in wynik:
            liczba+=x
        liczba=int(liczba)
        return liczba
    def m2(n):
        n= str(n)
        for x in range(len(n)-1):
            if int(n[x])>int(n[x+1]):
                return False
        return True
    def m3(n):
        array=[0,1,2,3,4,5,6,7,8,9]
        n= str(n)
        string=""
        for x in n:
            if int(x)==array[int(x)]:
                array[int(x)]=""
        for x in array:
            string+=str(x)
        return string
        
print(C.m1(4231564))
print()
print(C.m1(79381))
print()
print(C.m2(125579))
print()
print(C.m2(4557879))
print()
print(C.m3(23557))
print()
print(C.m3(12340))