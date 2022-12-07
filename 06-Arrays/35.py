def rand_elem(array):
    import random
    losowa= random.randint(0,len(array))
    element=array[losowa-1]
    return element

print(rand_elem(["pies","kot","kaczka","krowa",1,2,3,4,5,[6,6,6,6,6,6,6,6,6],["psy","koty","kaczki","krowy"]]))