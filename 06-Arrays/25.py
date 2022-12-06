def occurs(number, array):
    wynik=None
    for x in array:
        if number==x:
            wynik=True
    return wynik
        
array=[15, 38, 7, 23, 14]

number= (int(input("Enter number: ")))
czyjest=""
if occurs(number,array)==True:
    czyjest="appears in the array."
else: czyjest="does not appear in the array."
print(f"Number: {number}\nArray: {array}\nResult: number {number} {czyjest}")
