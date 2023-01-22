class C():
    def __init__(self,dictionary):
        self.dictionary=dictionary
        self.lista=""
        self.liczbaocen=0
        self.suma=0
    def m(self,n):
        for k,v in self.dictionary.items():
            for x in v:
                self.liczbaocen+=1
                self.suma+=x
            if self.suma/self.liczbaocen>=n:
                self.lista+=k+","  
            else:
                self.suma=0
                self.liczbaocen=0  
        self.lista=self.lista[:-1]
        return self.lista

s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
print(s.m(3))
print(s.m(4))
print(s.m(5))




        
