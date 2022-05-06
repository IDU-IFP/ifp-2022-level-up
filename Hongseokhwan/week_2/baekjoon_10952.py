# A+B - 5

a, b = [], [] # a, b 값을 저장할 배열 선언
res = [] # 합을 저장할 배열 선언

# 입력값의 합을 두 입력값이 0이 될때까지 반복해 저장
while(True):
    num1, num2 = map(int,input().split(" "))
    if(num1 == 0 and num2 == 0):
        break
    res.append(num1+num2)


# 여태 저장한 합들을 출력
for i in res:
    print(i)