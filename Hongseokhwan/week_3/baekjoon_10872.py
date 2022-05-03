# 팩토리얼

n = int(input()) # n 값 입력
res = 1 # 결과값을 저장할 변수 선언

# n 값을 1씩 줄여가며 res 값에 곱한 후 저장
for i in range(n, 0, -1):
    res *= i
    
# 출력
print(res)