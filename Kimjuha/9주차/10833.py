a=int(input())
total=0
for _ in range(a):
    student,apple=map(int,input().split())
    total+=apple%student

print(total)