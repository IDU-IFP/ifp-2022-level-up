# 정수가 순서대로 입력될 때 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단
# define : 정의하다
# 재귀함수

def goto(array, i):
  if array[i] == 0:
    return
  print(array[i])
  i += 1
  goto(array, i)

array = list(map(int, input().split()))
goto(array, i = 0)

# n개의 정수가 순서대로 입력될 때 n개의 입력된 정수를 순서대로 출력
n = int(input())
number = list(map(int, input().split()))

#1
print('== #1 ==')

def goto(number, n, i):
  if i == n: return
  print( number[i] )
  i += 1
  goto(number, n, i)

goto(number, n, 0)

#2 reverse 사용
print('== #2 ==')

number.reverse()
def goto(number, n):
  print(number[n])
  n -= 1
  if n == -1: return
  goto(number, n)

goto(number, n-1)

# 정수가 순서대로 입력될 때 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단
#1
number = map(int, input().split())

for element in number:
  if element is not 0:
    print(element)
    continue # continue를 만나면 아래의 구문은 실행하지 않고 다음 반복으로 넘어간다.
  break

#2
number = map(int, input().split())

for value in number:
  if value == 0: break
  print( value )

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력
count = int(input())

for i in range(count, 0, -1):
  print( i )

# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력
count = int(input())

for i in range(count-1, -1, -1):
  print( i )

# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력
converter = ord(input())

for i in range(97, converter+1):
  print( chr(i), end=' ' )

# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력
# while
count = int(input())

i = 0
while count >= 0:
  print( i )
  i += 1
  count -= 1

# for로 푸는 것이 더 간단
count = int(input())

for i in range(0, count+1):
  print( i )