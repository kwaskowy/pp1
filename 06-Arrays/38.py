def create_2d_arr(x,y):
    i= 0
    l= 0
    array=[]
    element=[]
    while l<y:
        element.append(0)
        l+=1
    while i<x:
        array.append(element)
        i+=1
    return array

print(create_2d_arr(3,5))