class C():
    def __init__(self,array):
        self.array=array
        self.string= ""
        self.suma=0
        for x in range(len(self.array)):
            if x==len(array)-1:
                self.string+=str(self.array[x])
                self.suma+=array[x]
            else:
                self.string+=str(self.array[x])
                self.string+="+"
                self.suma+=array[x]       
    def __str__(self):
        return f"{self.string}={self.suma}"
    
print(C([5,12]))
print(C([6,0,15]))
print(C([2,1,3,7]))