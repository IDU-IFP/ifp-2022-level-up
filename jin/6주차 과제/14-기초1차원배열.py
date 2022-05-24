# 이상한 출석 번호 부르기1

n = int(input())
rand = map(int, input().split())
student = [0 for _ in range(23)]
for r in rand:
  student[r-1] += 1
print(*student)

# 이상한 출석 번호 부르기2

n = int(input())
rand = list(map(int, input().split()))
rand.reverse()
print(*rand)

# 이상한 출석 번호 부르기3

n = int(input())
rand = map(int, input().split())
print( min(rand) )