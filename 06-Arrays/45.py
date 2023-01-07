def switcher(array):
    oneD=[]
    for x in array:
        for y in x:
            oneD.append(y)
    return oneD

print(switcher([[2,3],[1,5]]))
print(switcher([[5,0,3,7,5],[9,0,9,1,2]]))
print(switcher([[2,1],[3,5],[7,4],[2,6]]))