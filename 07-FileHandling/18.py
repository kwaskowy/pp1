firstfile= open("MeatAndFish.txt", "r")
secondfile= open("GrainsAndBread.txt", "r")
thirdfile= open("shoppinglist.txt", "a")
for line in firstfile:
    thirdfile.write(line)
for line in secondfile:
    thirdfile.write(line)
firstfile.close()
secondfile.close()
thirdfile.close()