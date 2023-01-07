array= [[7, 3, 7, 9, 0],
        [2, 9, 0, 1, 5],
        [3, 8, 6, 4, 7],
        [8, 7, 1, 1, 5]]
suma= 0
for x in array:
    for y in x:
        if y==x[-1]:
            suma+=y
print(suma)