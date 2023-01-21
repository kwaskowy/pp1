nr_konta= 12324567898765434567876545
numer=""
nr_konta= str(nr_konta)
i=0
for x in range(len(nr_konta)):
    if x==2 or x==6 or x==10 or x==14 or x==18 or x==22:
        numer+=" "
    numer+=nr_konta[x]
    
        
print(numer)