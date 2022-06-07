# 팩토리얼 0의 개수

res = 1 # 팩토리얼을 저장
count = 0 # 0의 개수

# 팩토리얼 계산
for num in range(2,int(input())+1):
    res *= num

s = str(res)[::-1] # 계산결과를 문자열로 변환

# 0의 개수를 세고 출력
for x in s:
    if(x == "0"):
        count += 1
    else:
        print(count)
        break