# 내 학점을 구해줘

t = int(input()) # 학기의 수 입력
res = [] # 결과를 담을 배열 선언

# 각 학기마다 학기의 정보를 입력받아 학점과 평균을 res 배열에 저장
for _ in range(0,t):
    c,g = 0,0
    for _ in range(int(input())):
        num1, num2 = map(float,input().split(" "))
        c += int(num1)
        g += num1 * num2
    
    res.append([c, g / c])

# 각 학기별 정보를 출력
for i in res:
    print("{} {:.1f}".format(i[0], i[1]))


