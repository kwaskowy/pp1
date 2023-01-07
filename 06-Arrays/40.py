array= [[-38, 19], 
        [5,   40],
        [-7,  11],
        [29,  16]]
max= 0
min = 66666
kolumna=1
wiersz=1
for x in array:
    for y in x:
        if y>max:
            max=y
        if y<min:
            min=y
for x in array:
    for y in x:
        if y==min:
            print(f"Smallest value is {min} and it is located in {kolumna} column and {wiersz} row.")
        if y==max:
            print(f"Largest value is {max} and it is located in {kolumna} column and {wiersz} row.")
        if kolumna==3:
            kolumna=1
        if kolumna==2:
            wiersz+=1
    kolumna+=1
    
