import sys
import math
n, k = map(int, input().split())  # nCr 공식을 이용
result = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
print(result)
