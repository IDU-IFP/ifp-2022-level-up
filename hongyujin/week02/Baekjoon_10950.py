t = int(input())

for _ in range(t):  # for 반복문 작성한다
    # split 함수를 이용해서 공백을 기준으로 두 문자열을 분리, 정수 변환을 위해 map함수를 이용
    a, b = map(int, input().split())
    print(a + b)
