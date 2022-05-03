# 정수형(int)으로 변수를 선언하고, 변수에 정수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력
var = int(input())
print(var)

# 문자형(char)으로 변수를 하나 선언하고, 변수에 문자를 저장한 후 변수에 저장되어 있는 문자를 그대로 출력
var = input()
print(var)

# 실수형(float)로 변수를 선언하고 그 변수에 실수값을 저장한 후 저장되어 있는 실수값을 출력
var = float(input())
print(var)

# 정수(int) 2개를 입력받아 그대로 출력
var = list(map(int, input().split()))
print(var[0], var[1])

# 2개의 문자(ASCII CODE)를 입력받아서 순서를 바꿔 출력
var = input().split()
print(var[1], var[0])

# 실수(float) 1개를 입력받아 저장한 후,
# 소수점 셋 째 자리에서 반올림하여 소수점 이하 둘 째 자리까지 출력
var = round(float(input()), 2)
print(var)

# int형 정수 1개를 입력받아 공백을 사이에 두고 3번 출력
var = int(input())
print(var, var, var)

# 어떤 형식에 맞추어 시간이 입력될 때, 그대로 출력
h, m = input().split(':')
print('{}:{}'.format(h, m))

# 년, 월, 일을 입력받아 지정된 형식으로 출력
y, m, d = input().split('.')
if len(m) == 1:
  m = '0'+m
if len(d) == 1:
  d = '0'+d
print('{}.{}.{}'.format(y, m, d))

# 주민번호 앞 6자리와 뒷 7자리가 '-'로 구분되어 입력
# '-'를 제외한 주민번호 13자리를 모두 붙여 출력
a, b = input().split('-')
print('{}{}'.format(a,b))

# 1개의 문자열을 입력받아 그대로 출력
string = input()
print(string)

# 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력
string = input().split('.')
print('''\
{}
{}
'''.format(string[0], string[1]))

# 입력받은 단어(영어)의 각 문자를 한줄에 한 문자씩 분리해 출력
string = input()
for i in range(len(string)):
  print("'{}'".format(string[i]))

# 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력
  integer = input()
count = len(integer)-1
for i in range(len(integer)):
  print([int(integer[i] + '0'*count)])
  count -= 1

# 입력되는 시:분:초 에서 분만 출력
  h, m, s = input().split(':')
print(m)

# 년월일(yyyy.mm.dd)를 입력받아, 일월년(dd-mm-yyyy)로 출력
y, m, d = input().split('.')
m = '0'+m if len(m) == 1 else m
d = '0'+d if len(d) == 1 else d
print('{}-{}-{}'.format(d, m, y))