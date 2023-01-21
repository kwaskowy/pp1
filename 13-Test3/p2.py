def f(arr):
    wynik=0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if (arr[-1][y]//arr[x][y])%(arr[y])!=0:
                wynik=0
            else: wynik+=1
    return wynik==0

print(f([[1,2,3],
        [2,4,6],
        [3,6,9]]) )
print(f([[1,2],[2,4]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]) )
print(f([[1,2],[3,6]]) )
print(f([[1,2,3],[2,4,6]]) )
print(f([[1,2,3],[2,5,6]]) )
