# 숫자의 개수

res = 1 # 세 수를 곱한 결과를 담을 변수 선언
num_arr = [0,0,0,0,0,0,0,0,0,0] # 숫자가 몇번 쓰였는지 카운트할 배열 선언

# 세 수를 입력받아 res 변수에 결과 담기
for _ in range(3):
    num = int(input())
    res *= num

# 결과값을 문자열로 형변환
res = str(res)

# 결과값의 한 문자와 배열의 인덱스를 비교해 같으면 해당 요소를 +1
for ch in res:
    for i in range(len(num_arr)):
        if(ch == str(i)):
            num_arr[i] = num_arr[i] + 1

# 배열을 반복해 출력
for num in num_arr:
    print(num)


