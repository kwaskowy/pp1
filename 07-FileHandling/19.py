file= open("integers.txt", "w")
for x in range(1,51,1):
        if x==50:
            file.write(str(x))
            break
        else:
            file.write(str(x)+"\n")
file.close()