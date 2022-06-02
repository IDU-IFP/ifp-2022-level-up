#https://www.acmicpc.net/problem/11170

for _ in range(int(input())):
    s = 0
    a,b = input().split()
    for i in range(int(a),int(b)+1):    # a ~ b
        s += str(i).count('0')  # count
    print(s)