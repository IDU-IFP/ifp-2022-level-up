#https://www.acmicpc.net/problem/10870
print(sum(W[7:]), sum(K[7:]))
n = int(input())
f1 = 0
f2 = 1
f3 = 1
for i in range(n-1):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
if n:
    print(f3)
else:
    print(0)
# for문 사용


def fibo(x):
    if x <= 1:
        return x
    else:
        return fibo(x-1) + fibo(x-2)


print(fibo(int(input())))
#재귀함수 사용
