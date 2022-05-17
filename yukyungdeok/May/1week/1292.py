# 1292번 쉽게 푸는 문제
a, b = map(int, input().split())

n = []

for i in range(b+1) :
  for j in range(i) :
    if b == len(n) :
      break
    n.append(i)
  
print(sum(n[a-1:b]))