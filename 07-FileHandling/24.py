import re
text= "To be, or not to be, that is the question"
vowels = re.findall("[a,o,e,i,y,u]",text)
ilosc= 0 
for x in vowels:
    ilosc+=1
print(f"In the text: {text}, there are {ilosc} vowels.")