# 뒤집힌 덧셈

# 두 수를 입력받아 뒤집어서 더한 후 그 값을 다시 뒤집어서 출력
num1, num2 = input().split()
res = str(int(''.join(reversed(num1)))+int(''.join(reversed(num2))))
print(int(''.join(reversed(res))))