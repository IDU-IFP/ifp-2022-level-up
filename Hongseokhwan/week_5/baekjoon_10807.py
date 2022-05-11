# 개수 세기

t = int(input()) # 입력할 정수의 개수
n = map(int, input().split(" ")) # t개 만큼 정수 입력
v = int(input()) # 찾고자 하는 정수 
count = 0 # n즁 v와 일치하는 정수의 개수

# n과 v를 입력해 일치하는 정수 찾기
for num in n:
    if(num == v):
        count += 1

# 개수 출력
print(count)
