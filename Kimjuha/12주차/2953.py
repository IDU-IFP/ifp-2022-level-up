winnerScore=0
for i in range(5):
    score=sum(list(map(int,input().split())))
    if score> winnerScore:
        winnerScore=score
        winner=i+1

print(winner,winnerScore)
