def f(array):
    zestringowane=""
    for x in array:
        x=str(x)
        zestringowane+=x+","
    zestringowane=zestringowane[:-1]
    return zestringowane
print(f([5,6,3,1,2,3]))

