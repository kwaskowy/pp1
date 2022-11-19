arr1 = [ [2,5,4] , [9,0,3] ]
print(arr1)
print(f"rows: {len(arr1)}, cols: {len(arr1[0])}")
print(arr1[0][1])
print(arr1[1][2])
for item in arr1[1]:
    print(item, end=" ")
print()
for y in arr1:
    for x in y:
        print(x, end=" ")
    print()
for y in arr1:
    print(y[2])