# 지능형 기차

res = 0 # 최대 사람 수를 담을 변수 선언
sum = 0 # 기차에 타고있는 사람 수를 담을 변수 선언

# 역마다 내리고 탄 사람의 수를 계산하고 비교해 최대 사람 수 찾기
for _ in range(4):
    down, up = map(int,input().split(" "))
    sum = sum - down + up

    if(res < sum):
        res = sum

# 출력
print(res)
