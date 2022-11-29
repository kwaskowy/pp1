def compare(array1,array2):
    czytesame=None
    if len(array1)==len(array2) and array1[0]==array2[0] and array1[len(array1)]==array2[len(array2)]:
        czytesame=True
    else: czytesame=False
    return czytesame


array1=[True,False]  
array2=[True,False,True]


tab1=""
tab2=""
wynik=""
if compare(array1,array2)==True:
    wynik+="the same"
else: wynik+="not the same"
for x in array1:
    tab1+= str(x)+" "
for x in array2:
    tab2+= str(x)+" "
print(f"Array1: {tab1}\nArray2: {tab2} \nComparison: arrays are {wynik}")