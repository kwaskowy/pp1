def bubblesort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                zmiana= array[j]
                array[j]=array[j+1]
                array[j+1]= zmiana
    return array

array=[1,3,45,10,6,34,21,4,15,3,69,51,39,12,21]
array2=[3,5,67,523,235,3457,75,43,643,346,63,4,475,568,7,23,235,352,3,74,58,64,795,579,47]
array3=[5,6,7,23,4,5,2,1,5,67,36,4,43,34,123,62,7,3]
print(bubblesort(array))
print(bubblesort(array2))
print(bubblesort(array3))