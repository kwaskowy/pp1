from bank import Account
user1= Account(12345655559090111100007722)
user1.display()
print()
user1.deposit(25.30)
user1.display()
print()
user1.withdraw(31.70)
user1.withdraw(14)
print()
user1.display()
print()

print("Second account:")
user2= Account(12345687654320009876789876)
user2.deposit(666.66)
user2.display()