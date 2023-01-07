array= [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]

print("An array before swap:")
for x in array:
    for y in x:
        print(y, end=" ")
        if y%5==0:
            print()
pamiec= []
pamiec= array[0]
array[0]=array[2]
array[2]=pamiec
print()
print()
print("An array after swap:")
for x in array:
    for y in x:
        print(y,end=" ")
    if y%5==0:
        print()