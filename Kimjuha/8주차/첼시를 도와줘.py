case = int(input())

for _ in range(case):
    n = int(input())
    members = []
    for i in range(n):
        members.append(list(input().split()))
        members[i][0] = int(members[i][0])

    members.sort()
    print(members[-1][1])
