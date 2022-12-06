array=[5,1,9,10,11,15,32]
najwieksza=0
druga=0
for x in array:
    if x>najwieksza:
        najwieksza=x
for x in array:
    if x<najwieksza and x>druga:
        druga=x
print(f"Największa wartość: {najwieksza}, druga największa: {druga}")