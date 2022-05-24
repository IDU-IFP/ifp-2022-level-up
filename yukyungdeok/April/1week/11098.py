#11098번 첼시를 부탁해
n = int(input())

for i in range(n):
    player = int(input())
    max_price = 0
    max_name = ""
    for i in range(player):
        cost, name = input().split()
        if (int(cost) > max_price):
            max_price = int(cost)
            max_name = name
    print(max_name)