# 잃어버린 괄호
# 덧셈을 먼저 한 후에 뺄셈을 해 최소의 결과값을 구하는 방법을 사용

m = input() # 식 입력
sign = [] # 부호를 담을 배열
num = [] # 숫자를 담을 배열
index = 0 # 인덱스
count = 0 # 부호 카운트
hap = [] # 숫자들의 합을 담을 배열
res = 0 # 결과값

for i in range(len(m)): # 부호를 기준으로 해서 부호와 숫자를 각각의 배열에 저장
    if(m[i] == "+" or m[i] == "-"):
        sign.append(m[i])
        num.append(int(m[index:i])) 
        index = i+1

num.append(int(m[index:])) # 반복문으로 저장이 안되는 마지막 숫자도 저장

for i in range(len(sign)): # 부호별로 계산
    if(sign[i] == "+"): # 덧셈
        if(i == len(sign)-1): # 덧셈이 식의 마지막 부호라면
            hap.append(sum(num[i-count:i+2])) # 덧셈 양 옆에 있는 숫자를 더해 합 배열에 저장
        count += 1 # 덧셈이 연속으로 나올수 있으므로 부호 카운트
    else: # 뺄셈
        if(len(sign) == 1): # 부호가 단 한개라면
            res = num[0] - num[1] # 숫자 배열에 있는 두 수를 바로 뺄셈해 결과값에 저장
        else: # 부호가 여러개라면
            hap.append(sum(num[i-count:i+1])) # 뺄셈 전까지 나온 수들을 다 더한 후 합 배열에 저장
            count = 0 # 덧셈 카운트 초기화
        if(len(sign) != 1 and i == len(sign)-1): # 뺄셈이 마지막 부호라면
            hap.append(num[i+1]) # 합 배열에 저장

if(len(sign) == 0): # 부호 없이 숫자만 있다면
    print(num[0]) # 숫자만 출력
elif(len(hap) == 0): # 합 배열에 저장된 숫자가 없다면 뺄셈 부호 하나만 있는 식이므로
    print(res) # 위에서 받은 결과값 그대로 출력
else: # 숫자, 부호 여러개가 혼합된 식이라면
    for i in range(len(hap)): # 합 배열 숫자 반복
        if(i == 0): # 첫 숫자를 제외한 모든 숫자는 뺄셈처리
            res += hap[i]
        else:
            res -= hap[i]
        
    print(res) # 결과값 출력