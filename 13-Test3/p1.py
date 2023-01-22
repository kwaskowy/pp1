def f(n):
    i=0
    string=""
    while i<n:
        string+="/"
        i+=1
        if i%5==0:
            string+="-"
        if i==n and n%5==0:
            string=string[:-1]
    return string

print(f(15))
