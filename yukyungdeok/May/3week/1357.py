# 1357번 뒤집힌 덧셈
x, y = map(str, input().split())
n = str(int(x[::-1]) + int(y[::-1]))
print(int(n[::-1]))