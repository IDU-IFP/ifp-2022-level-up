# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력
#1
a, b, c = map(int, input().split())
if not a%2: print(a)
if not b%2: print(b)
if not c%2: print(c)

#2
a, b, c = map(int, input().split())
print( *(filter(lambda num: num%2 == 0, [a, b, c])) )

# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력
#1
a, b, c = map(int, input().split())
print( 'odd' if a%2 else 'even' )
print( b%2 and 'odd' or 'even' )
print( ['even', 'odd'][c%2] )


#2
a, b, c = map(int, input().split())
print( *map(lambda num: 'odd' if num%2 else 'even', [a, b, c]) )

# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력
num = int(input())
print( num>0 and 'plus' or 'minus' )
print( num%2 and 'odd' or 'even' )

# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력
grade = int(input())
if grade >= 90:
  print('A+')
elif grade >= 70:
  print('B')
elif grade >= 40:
  print('C')
else:
  print('D')

# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력
word = input()
if word == 'A':
  print('best!!!')
elif word == 'B':
  print('good!!')
elif word == 'C':
  print('run!')
elif word == 'D':
  print('slowly~')
else:
  print('what?')

# 월이 입력될 때 계절 이름이 출력
# 1
month = int(input())
if month==12 or month==1 or month==2:
  print('winter')
elif month==3 or month==4 or month==5:
  print('spring')
elif month==6 or month==7 or month==8:
  print('summer')
else:
  print('fall')

# 2
if month in [12,1,2]:
  print('winter')
elif month in [3,4,5]:
  print('spring')
elif month in [6,7,8]:
  print('summer')
else:
  print('fall')