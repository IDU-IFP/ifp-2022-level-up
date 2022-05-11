A, B = input().split()
A = int(A[::-1])  # 역순 : [::-1]
B = int(B[::-1])

if A > B:  # 변환된 숫자 크기 비교
    print(A)
else:
    print(B)
