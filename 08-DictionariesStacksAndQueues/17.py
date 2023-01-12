import json
file= open("euro.json","r",encoding="UTF-8")
filecontent= json.load(file)
for k,v in filecontent.items():
    for x in v:
        limited_values={"Data":x["Data"],"mid":x["mid"]}
        print("\n")
        for z,y in limited_values.items():
            if z=="mid":
                z="Wartość"
            print(z,":",y)
            
            
        
    
        