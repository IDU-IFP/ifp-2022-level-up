age = int(input())
balance = 9000
if age>=19:
    balance=balance-1250
elif 13<=age<=18:
    balance=balance-1050
else:
    balance=balance-650
print(balance)
