import json
file= open('example.json',"r")
data = json.load(file)
file.close()
for k,v in data.items():
    print(k,":",v,)
    
