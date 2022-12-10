array=[{"country":"Poland","population":"38mln"},{"country":"Germany","population":"83mln"},{"country":"Sweden","population":"10mln"},{"country":"Greece","population":"10mln"},{"country":"France","population":"67,5mln"}]

lenght=len(array)
while lenght>0:
    for k,v in array[lenght-1].items():
        print(k,":",v)
    print("")
    lenght-=1