#https://www.acmicpc.net/problem/2587

arr = [0,0,0,0,0]
for i in range(5):
    n = int(input())
    arr[i] = n

arr.sort()

print(sum(arr)//5)
print(arr[2])