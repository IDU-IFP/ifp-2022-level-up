# from itertools import permutations
# from collections import deque

# o = ["+", "-", "*", "/"]
# x = int(input())
# numbers = list(map(int, input().split()))
# oper_nums = list(map(int, input().split()))
# opers, results = [], []

# for a, b in enumerate(oper_nums):
#     opers.extend([o[a]] * b)

# for set in set(permutations(opers, x - 1)):
#     tmp = deque(set)
#     tmp_nums = deque(numbers)
    
#     s = tmp_nums.popleft()
#     while len(tmp) != 0:
#         t = tmp.popleft()
#         n = tmp_nums.popleft()

#         if t == o[0]:
#             s += n
#         if t == o[1]:
#             s -= n
#         if t == o[2]:
#             s *= n
#         if t == o[3]:
#             if s < 0:
#                 s = int((s * -1) / n) * -1
#             else:
#                 s = int(s / n)

#     results.append(s)

# print(max(results))
# print(min(results))

# dfs 사용

n = int(input())
numbers = list(map(int, input().split()))
p, m, d, t = map(int, input().split())
results = []

def dfs(s, tmp):
    global p, m, d, t
    if s == n:
        results.append(tmp)
        return

    if p > 0:
        p -= 1
        dfs(s + 1, tmp + numbers[s])
        p += 1
    if m > 0:
        m -= 1
        dfs(s + 1, tmp - numbers[s])
        m += 1
    if d > 0:
        d -= 1
        dfs(s + 1, tmp * numbers[s])
        d += 1
    if t > 0:
        t -= 1
        dfs(s + 1, int(tmp / numbers[s]))
        t += 1

dfs(1, numbers[0])
print(max(results))
print(min(results))
    