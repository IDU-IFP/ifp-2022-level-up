n=int(input())

for _ in range(n):
    p=int(input())
    CostList=[]
    PlayerList=[]
    for _ in range(p):
        cost,Player=input().split()
        Cost=int(cost)
        CostList.append(Cost)
        PlayerList.append(Player)

    idx=CostList.index(max(CostList))
    print(PlayerList[idx])