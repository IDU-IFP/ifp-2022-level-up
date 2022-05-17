n = int(input())
rand = map(int, input().split())
student = [0 for _ in range(23)]
for r in rand:
    student[r-1] += 1
print(*student)
