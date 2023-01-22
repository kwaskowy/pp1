def f(arr):
    suma_col= 0
    suma_wiersz= 0
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if x==0:
                suma_wiersz+=arr[x][y]
            if y==0:
                suma_col+=arr[x][y]
    return suma_col==suma_wiersz

print(f([[1,2,3],
        [2,4,6],
        [3,6,9]]) )
print(f([[1,2],[2,4]]))
print(f([[1,2,3,4],[2,4,6,8],[3,6,9,12],[4,8,12,16]]) )
print(f([[1,2],[3,6]]) )
print(f([[1,2,3],[2,4,6]]) )
print(f([[1,2,3],[2,5,6]]) )
