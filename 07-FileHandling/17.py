firstfile= open("rickroll.txt", "r")
secondfile= open("copylines.txt", "w")
for line in firstfile:
    secondfile.write(line)
firstfile.close()
secondfile.close()
