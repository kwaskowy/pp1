def star(n):
    gwiazdki=""
    gwiazdki+=n*("*")
    return gwiazdki

arr= [12, 6, 4, 9, 10]

for x in arr:
    print(f"{x}:{star(x)}")

