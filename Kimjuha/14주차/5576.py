scoreW=[]
scoreK=[]
for i in range (10):
    scoreW.append(int(input()))
for i in range (10):
    scoreK.append(int(input()))
scoreK.sort()
scoreW.sort()
print(sum(scoreW[-3:]),sum(scoreK[-3:]))