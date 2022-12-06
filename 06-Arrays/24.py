lista=[2,3,2,5,6,1,8,8,9,1]
unikatowe=[]

for x in lista:
    if x not in unikatowe:
        unikatowe.append(x)
print(unikatowe)