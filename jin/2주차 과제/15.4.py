age = int(input())
balance = 9000 #교통카드 잔액

if 6 < age:
    if 7 <= age <= 12:
        balance -= 650
    elif 13 <= age <= 18:
        balance -= 1050
    elif 19 <= age:
        balance -= 1250
        
    print(balance)