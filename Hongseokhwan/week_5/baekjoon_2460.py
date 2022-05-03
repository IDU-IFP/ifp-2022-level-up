# 지능형 기차 2

sum = 0 # 기차 내부에 있는 사람의 수를 담을 선언
res = 0 # 최대값을 담을 변수 선언

# 10개의 역을 다니면서 기차 내부에 있는 사람의 수의 최대값 구하기
for _ in range(10):
    down, up = map(int, input().split(" "))
    sum = sum - down + up
    if(sum > res):
        res = sum

# 출력
print(res)