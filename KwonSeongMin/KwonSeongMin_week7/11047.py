#https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

n,k=map(int,input().split())
count = 0
money = [0 for _ in range(n)]
for i in range(n):
    money[i] = int(input())
    
money.sort(reverse=True)

for m in money: 
    if m <= k:  # money값이 k값보다 작으면, 예시를 들면 k = 4790 이고 m = 1000 일 때
        count += k//m   # k // m 값을 count, 4
        k -= (k//m)*m   # k에서 4 * 1000 의 값을 빼준다.

print(count)
            