# 2953번 나는 요리사다
li = []

for _ in range(5):
    li.append(sum(map(int,input().split())))
    
print(li.index(max(li))+1,max(li))