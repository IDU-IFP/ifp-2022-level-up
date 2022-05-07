# 정수 2개를 입력받아 합을 출력하는 프로그램
a, b = map(int, input().split())
print( a+b )

# 정수 2개를 입력받아 합을 출력하는 프로그램
a, b = map(int, input().split())
print( a+b )

# 입력된 정수의 부호를 바꿔 출력
intConv = -int(input())
print( intConv )

# 영문자 1개를 입력받아 그 다음 문자를 출력
order = ord(input())
print( chr(order+1) )

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력
a, b = map(int, input().split())
print( a//b )

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력
a, b = map(int, input().split())
print( a%b )

# 정수를 1개 입력받아 1만큼 더해 출력
a = int(input())
print( a+1 )

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산
a, b = map(int, input().split())
print( a+b )
print( a-b )
print( a*b )
print( a//b )
print( a%b )
print( round(a/b, 2) )

# 정수 3개를 입력받아 합과 평균을 출력
a, b, c = map(int, input().split())
print( a+b+c )
print( round((a+b+c)/3, 1) )