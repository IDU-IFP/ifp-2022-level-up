# 콘테스트

w = [] # w 대학교 점수를 담을 배열
k = [] # k 대학교 점수를 담을 배열

# w 대학교 점수 입력
for _ in range(10):
    w.append(int(input()))

# k 대학교 점수 입력
for _ in range(10):
    k.append(int(input()))

# 각 대학교의 상위 점수 3개의 합을 출력
print(sum(sorted(w)[7:]), sum(sorted(k)[7:]))