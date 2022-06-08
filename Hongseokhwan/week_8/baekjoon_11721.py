# 열 개씩 끊어 출력하기

ment = input() # 문장 입력

# 열 개씩 끊어서 출력
for i in range(0,len(ment),10):
    print(ment[i:i+10])