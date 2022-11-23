arr1= ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest= ""
for x in arr1:
    if len(x)>len(longest):
        longest=x
print(longest)