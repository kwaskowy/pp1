array=[5,1,9,6,1]
najmniejsza=66666**66666
największa=0
for x in array:
    if x>największa:
        największa=x
for x in array:
    if x<najmniejsza:
        najmniejsza=x
różnica=największa-najmniejsza
print(f"Array: {array}\nResult: {różnica}") 
