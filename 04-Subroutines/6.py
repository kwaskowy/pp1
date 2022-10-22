def keypad():
    for num in range(1,10,1):
        print(num, end=" ")
        if num%3==0:
            print()
keypad()