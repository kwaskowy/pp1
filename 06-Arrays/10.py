arr1= [60,3,5,6,7,8,1,41,21,64,856,234142,124,412,124,14,212]
even=0
odd=0
i=0
q=0
while len(arr1)>i:
    i+=1
    if arr1[q]%2==0:
        even+=1
        q+=1
    else:
        q+=1
        odd+=1
print(f"even numbers: {even} \nodd numbers: {odd}")
