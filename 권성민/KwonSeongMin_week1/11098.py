#https://www.acmicpc.net/problem/11098

n = int(input())
for _ in range(n):
    money = []
    player = []
    p = int(input())
    for i in range(p):
        inp = input().split()
        
        money.append(int(inp[0]))
        player.append(inp[1])
        
        res = max(money)
        player_res = money.index(res)

    print(player[player_res])
        