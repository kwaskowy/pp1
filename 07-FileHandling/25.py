import re
text= "To be, or not to be, that is the question"
words= re.findall("[ ]", text)
slowa=1
for x in words:
    slowa+=1
print(f"There are {slowa} words in following text: {text}")