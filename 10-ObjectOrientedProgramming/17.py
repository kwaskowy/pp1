class Statistics():
    def __init__(self):
        self.numbers= []
        self.great= (-666)*666
        self.small= 666*666
        self.arithm= 0
        self.mediana=0
    def display_nums(self):
        for x in range(len(self.numbers)):
            print(self.numbers[x],end=" ")
    def add(self):
        self.numbers.append(int(input("Input number: ")))
    def greatest(self):
        for x in self.numbers:
            if x>self.great:
                self.great=x
        print(f"Greatest value found. It is {self.great}")
    def smallest(self):
        for x in self.numbers:
            if x<self.small:
                self.small=x
        print(f"Smallest value found. It is {self.small}")
    def arithmetic_mean(self):
        suma=0
        for x in self.numbers:
            suma+=x
        self.arithm=suma/(len(self.numbers))
        print(f"The arithmetic mean is {self.arithm}")
    def median(self):
        import statistics
        self.mediana=statistics.median(self.numbers)
        print(f"Median is {self.mediana}")
    def display_statistical(self):
        print()
        print(f"In following array: {self.numbers}\nGreatest value is {self.great}\nSmallest value is {self.small}\nArithmetic mean is {self.arithm}\nMedian is {self.mediana}")

staty= Statistics()
i=0
while i<10:
    staty.add()
    i+=1
staty.display_nums()
print()
staty.greatest()
staty.smallest()
staty.arithmetic_mean()
staty.median()
print()
staty.display_statistical()