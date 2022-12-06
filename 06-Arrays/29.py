given=input("Input number:")
given=int(given)
HowManyElements=0
array=[5,15,1.35,35,13,41,143,2.35,543.543,346,13.4,123,142,51.23,62.467,35,253,12.4,1.23,23.5,23.6]
for x in array:
    if x>given:
        HowManyElements+=1
print(f"Number of elements in array: {len(array)}\nNumber of elements greater than given number: {HowManyElements}")