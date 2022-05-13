# 약수

n = int(input()) # 약수의 개수 입력
a = list(map(int, input().split())) # 약수를 입력해 배열에 저장

# 결과 출력
if(len(a) == 1):
    print(a[0]**2)
else:
    print(max(a) * min(a))