filename = input("Enter filename:")
file = open(filename, "r")
suma= 0 
for line in file:
    suma+=1
print(f"File name: {filename}\nNumber of lines in file:{suma}")
file.close()
