firstfile= open("rickroll.txt", "r")
secondfile= open("copy.txt", "w")
file_content = firstfile.read()
secondfile.write(file_content)
firstfile.close()
secondfile.close()