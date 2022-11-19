arr1 = [1,2,3,4,5]
print(arr1)
arr1[0]= arr1[0]-1
print(arr1)
arr1[-1]= arr1[-1]+4
print(arr1)
arr1[len(arr1)//2]= arr1[len(arr1)//2] *2
print(arr1)
arr1 = [x+3 for x in arr1]
print(arr1)
for i in range(len(arr1)):
    arr1[i] +=3
print(arr1)