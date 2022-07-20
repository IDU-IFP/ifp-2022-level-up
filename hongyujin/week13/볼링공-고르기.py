n, m = map(int, input().split())  # 볼링공의 개수, 공의 최대 무게
k = list(map(int, input().split()))  # 볼리공의 무게

count = 0
for i in range(n-1):  # 1번 볼링공부터 n-1 볼링공까지
    for j in range(i+1, n):
        if k[i] != k[j]:  # 하나씩 비교하며 볼링공의 무게가 같으면 넘어가고
            count += 1   # 다르면 count 변수에 1씩 증가

print(count)
