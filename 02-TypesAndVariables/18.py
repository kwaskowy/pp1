import math
a = int(input("Podaj bok a:"))
b = int(input("Podaj bok b:"))
c = int(input("Podaj bok c:"))
p = 1/2*(a+b+c)
P = int(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(f"Pole wynosi {P}")