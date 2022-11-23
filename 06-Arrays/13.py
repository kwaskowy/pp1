arr=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
suma=0
for x in arr:
    for y in x:
        if y%2==0:
            suma+=y
print(f"suma parzystych: {suma}")
