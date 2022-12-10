array=["shrek","shrek 2","shrek 3","shrek forever","it"]

file = open("films.txt","w")
for title in array:
    file.write(title+"\n")
file.close()