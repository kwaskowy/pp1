from re import X


arr1= [-15,8,-31,47,-2,19]
max= arr1[0]
min= arr1[0]
for i in range(1,len(arr1)):
    if arr1[i]>max:
        max=arr1[i]
    if arr1[i]<min:
        min=arr1[i]

print(f"max = {max}, min={min}")