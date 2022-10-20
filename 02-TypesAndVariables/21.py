from random import randint
throw = randint(1,6)
guess = int(input("Wybierz liczbę oczek od 1 do 6:"))
print(throw==guess)