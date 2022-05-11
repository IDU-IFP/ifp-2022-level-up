A = int(input())              # 150
B = int(input())              # 266
C = int(input())              # 427
gop = list(str(A * B * C))    # [1,7,0,3,7,3,0,0]

for i in range(10):
    print(gop.count(str(i)))  # count함수를 이용하여i를 str(문자열)로 바꿔서 출력
