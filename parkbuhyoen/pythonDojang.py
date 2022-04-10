#문제 3.7  , 3.8
'''
print('Hello, world!')
print('Python Programming')
'''
#문제 5.6
'''
AP=102
print(AP * 0.6 + 225)
'''
#문제 6.7
'''
a=50
b=100
c=None

print(a)
print(b)
print(c)
'''
#6.8 심사문제: 평균 점수 구하기
'''
a,b,c,d = map(int,input().split())

average=(a+b+c+d)//4

print(average)
'''
#7.5 심사문제: 날짜와 시간 출력하기
'''
year, month, day, hour, minute, second = input().split()

print(year, month, day,sep='-',end='T')
print(hour, minute, second, sep=':')
'''
#8.5 심사문제: 합격 여부 출력하기
'''
k,e,m,s = map(int,input().split())
if k>=90 and e>80 and m>85 and s>=80:
    print("True")
else:
    print("False")
'''
#9.4 심사문제: 여러 줄로 된 문자열 사용하기
'''
s="""'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively."""
print(s)
'''
#10.5 심사문제: range로 튜플 만들기
'''
a=int(input())
result = tuple(range(-10, 10, a))
print(result)
'''
#11.8 심사문제: 리스트의 마지막 부분 삭제하기
'''
x = input().split()
print(tuple(x[0:len(x)-5]))
'''
#11.9 심사문제: 문자열에서 인덱스가 홀수인 문자와 짝수인 문자 연결하기
'''
a = input()
b = input()

f=a[1:len(a):2]
d=b[0:len(b):2]

print(f+d)
'''
#12.5 심사문제: 딕셔너리에 게임 캐릭터 능력치 저장하기
'''
x1=input().split()
x2=map(float,input().split())

print(dict(zip(x1,x2)))
'''