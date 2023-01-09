file= open("powers.txt", "w")
for x in range(1,11,1):
    if x==10:
        file.write(str(x)+","+str((x**2))+","+str((x**3)))
        break
    else:
        file.write(str(x)+","+str((x**2))+","+str((x**3))+"\n")
file.close()