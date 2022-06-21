case = int(input())

for i in range (case):
    a, b = map(int, input().split())
    c = a % b
    d = a //b
    print("You get %d piece(s) and your dad gets %d piece(s)."%(d,c))