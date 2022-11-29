arr=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for item in arr:
    liczba=0
    for x in item:
        if arr[liczba][liczba]==0:
            arr[x+liczba][liczba]=1
            liczba+=1
for item in arr:
    for x in item:
        print(x, end=" ")
    print()
        
        
