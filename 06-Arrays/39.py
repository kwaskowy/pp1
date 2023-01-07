array=[[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
mnożnik= 1
numerek=1
miejsce_w_rzędzie=0
for x in array:
    for y in x:
        x[y+miejsce_w_rzędzie]= numerek*mnożnik
        numerek+=1
        if miejsce_w_rzędzie==4:
                miejsce_w_rzędzie=0
                numerek=1
                mnożnik+=1
        else:
            miejsce_w_rzędzie+=1
print(array)