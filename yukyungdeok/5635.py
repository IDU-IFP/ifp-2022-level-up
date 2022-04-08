# 5635번 생일
Students = []

for i in range(int(input())):
    name, day, month, year = input().split()
    Students.append([name, int(day), int(month), int(year)])

Students.sort(key = lambda x:(x[3], x[2], x[1]))

print(Students[-1][0])
print(Students[0][0])