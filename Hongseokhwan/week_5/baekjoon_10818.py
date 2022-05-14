# 최소, 최대

t = int(input()) # 정수의 개수
n = sorted(map(int, input().split())) # t개의 정수를 입력받고 오름차순으로 정렬
print(n[0], n[t-1]) # 최소값, 최대값 출력