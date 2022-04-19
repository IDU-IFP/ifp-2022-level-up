#acmicpc.net/problem/2921
sum = 0
for i in range(1,int(input())+1):
    sum += i
    for j in range(i+1):
        sum += i+j
print(sum)  # 시간복잡도 = O(n^2)
#other's code
num = int(input())
print((num*(num+1)*(num+2))//2) # 시간복잡도 = O(1)