from random import randint
file= open("randomintegers.txt", "w")
losowa= randint(100,999)
for x in range(1,51,1):
        if x==50:
            losowa= randint(100,999)
            file.write(str(losowa))
            break
        else:
            file.write(str(losowa)+"\n")
            losowa= randint(100,999)
file.close()