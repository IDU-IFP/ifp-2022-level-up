# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구하기
num = int(input())

print('== #1 ==')
#1
answer = 0
for i in range(2, num+1, 2):
  answer += i
print(answer)

print('== #2 ==')
#2
answer2 = [i for i in range(2, num+1, 2)]
print( sum(answer2) )

print('== #3 ==')
#3
answer3 = range(2, num+1, 2)
print( sum(answer3) )

# 원하는 문자가 입력될 때까지 반복 출력하기
# 'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램
word = input().split()

print('== #1 ==')
#1
for w in word:
  print(w)
  if w == 'q': break

print('== #2 ==')
#2
i = 0
while word[i] != 'q':
  print(word[i])
  i += 1
print(word[i])

# 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램
end_point = int(input())

print('== #1 ==')
#1
total = 0
i = 0
while total < end_point:
  i += 1
  total += i
print( i )

print('== #2 ==')
#2
total = 0
for i in range(1, end_point+1):
  total += i
  if total >= end_point:
    print( i )
    break

# 주사위를 2개 던지면? 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력
n, m = map(int, input().split())

for n in range(1, n+1):
  for m in range(1, m+1):
    print(n, m)

# A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력
char = input()

for i in range(1, 16):
  print( '%s*%s=%s' %(char, hex(i)[2:].upper(), hex(int(char, 16) * i)[2:].upper()) )

# 3 6 9 게임의 왕이 되기 위한 마스터 프로그램
num = int(input())

print('== #1 정답 ==')
#1
for i in range(1, num+1):
  count = i if i%3 else 'X'
  print(count, end=' ')

print('\n== #2 오답 ==')
#2
for i in range(1, num+1):
  count = 'X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i
  print(count, end=' ')

# 빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때, 주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓 수를 계산
r, g, b = map(int, input().split())

count = 0
for i in range(r):
  for j in range(g):
    for k in range(b):
      print(i, j, k)
      count += 1
print(count)

# 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())

result = h*b*c*s
resultMB = result / (8 * 1024**2)
print(round(resultMB, 1), 'MB')

# 그림 파일 저장용량 계산하기
w, h, b = map(int, input().split())
result = (w*h*b) / (8 * 1024**2)
print( round(result, 2), 'MB' )

# 1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램
end_point = int(input())
total = 0
i = 1
while total < end_point:
  total += i
  i += 1
print( total )

# 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않음
num = int(input())

for i in range(1, num+1):
  if i%3:
    print(i, end=' ')

# 시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램
a, d, n = map(int, input().split())

i = a
count = 0
arith = []
while count < n:
  arith.append(i)
  i += d
  count += 1
print( arith[-1] )

# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램
a, r, n = map(int, input().split())

i = a
count = 0
geom = []
while count < n:
  geom.append(i)
  i *= r
  count += 1
print( geom[-1] )

# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램
a, m, d, n = map(int, input().split())

i = a
prog = []
while len(prog) < n:
  prog.append(i)
  i = i*m+d
print( prog[-1] )

# 세 방문 주기의 최소 공배수를 구해보자
a, b, c = map(int, input().split())
day = 1
while day%a != 0 or day%b != 0 or day%c != 0:
  day += 1
print( day )

day = 1
while 1:
  day += 1
  if day%a == 0 and day%b == 0 and day%c == 0: break
print( day )