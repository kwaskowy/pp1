file = open("30lines.txt")
licznik= 0
while licznik<30:
    print(file.readline())
    licznik+=1
    if licznik==30:
        break
    if licznik%5==0:
        x = input("press enter to continue...")
    else: continue
file.close()