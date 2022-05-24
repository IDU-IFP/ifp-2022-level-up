# 1427번 소트인사이드
n = int(input())
li = []
li = list(map(int, str(n)))
li.sort(reverse=True)
for n in li:
    print(n, end="")