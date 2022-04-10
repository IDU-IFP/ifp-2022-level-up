# 최대공약수와 최소공배수

x,y = input().split(" ") # 두 개의 자연수 입력

# 정수형 변환
x = int(x) 
y = int(y)

min = 0 # 최소공배수를 담을 변수
max = 0 # 최대공약수를 담을 변수

# 두 자연수 중 큰 값을 x에, 작은 값을 y에 저장
if(x<y):
    temp = x
    x = y
    y = temp

# 최소공배수를 위해 x, y의 배수를 리스트에 저장
x_mul = [x*i for i in range(1,y+1)]
y_mul = [y*i for i in range(1,x+1)]

# 리스트 요소 순차적으로 비교하며 같은 값(=최소공배수) 찾기
for i in range(len(x_mul)):
    for j in range(len(y_mul)):
        if(y_mul[j] == x_mul[i]):
            min = y_mul[j]

    # 최소공배수가 저장된 즉시 반복문 탈출
    if(min):
        break

# 두 자연수 중 작은 수만큼 반복을 돌려 둘다 나머지가 0인 값(=최대공약수) 찾기
for i in range(1,y+1):
    if(x % i == 0 and y % i == 0):
        max = i
        
# 최소공배수, 최대공약수 출력
print(max)
print(min)
