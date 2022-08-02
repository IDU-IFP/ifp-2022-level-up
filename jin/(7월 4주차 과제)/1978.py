T = int(input())
List1 = list(map(int, input().split()))
A = 0

def isprime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    else:
        False

for j in List1:
    if isprime(j) == True:
        A += 1

print(A)