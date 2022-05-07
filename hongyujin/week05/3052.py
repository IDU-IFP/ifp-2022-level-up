n = []

for _ in range(10):  # for문 0~9
    a = int(input())  # 정수 입력
    b = a % 42
    n.append(b)  # [1,2,3,4,5,6,7,8,9,10]

s = set(n)  # n에 저장된 자료형의 중복을 제거 해주는 함수 이용
print(len(s))  # len 함수 이용해서 s의 길이 출력
