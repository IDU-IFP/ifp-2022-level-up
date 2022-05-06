n = [int(input()) for _ in range(10)]
print(sum(n)//10)  # 평균
print(max(n, key=n.count))  # 최빈값, max 함수의 key 파라미터 이용
