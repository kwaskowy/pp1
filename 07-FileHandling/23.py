import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
wynik= 0 
for x in temperatures:
    wynik+= int(x)
wynik=wynik//3
print(f"Average temperature is {wynik}C")