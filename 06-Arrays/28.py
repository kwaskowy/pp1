def median(array):
    if len(array)%2==0:
        mediana=(array[(len(array)//2)-1]+array[(len(array)//2)])/2
    else: mediana=array[len(array)//2]
    return mediana
    


print(median([5,5,6,5]))
print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))

        