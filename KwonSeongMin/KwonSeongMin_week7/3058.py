#https://www.acmicpc.net/problem/3058

for _ in range(int(input())):
    arr = []
    n = list(map(int,input().split()))
    for num in n: 
        if num%2 == 0:   
            arr.append(num)
    print(sum(arr),min(arr))