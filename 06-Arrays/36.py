array= [[1,2,3,4],
        [5,6,7,8]]

for x in array:
    for y in x:
        print(y, end=" ")
        if y%4==0:
            print()