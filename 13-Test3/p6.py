class C():
    def __init__(self,n):
        self.liczba=n
    def m1(self):
        return self.liczba
    def m2(self):
        self.liczba+=1
    def m3(self):
        self.liczba-=1
    def m4(self,n):
        self.liczba+=n

c= C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())