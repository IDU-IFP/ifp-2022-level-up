# 10872번 팩토리얼

n = int(input())
a = 1
if n > 0:
    for i in range(1, n+1):
        a *= i
print(a)