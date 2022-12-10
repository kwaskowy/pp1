add = input("Enter name of product: ")
file= open("shopping.txt","a")
file.write(add+"\n")
file.close()