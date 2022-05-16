# 2309번 일곱 난쟁이
li = []
for _ in range(9):
    li.append(int(input()))
for i in li:
    for j in li:
        if sum(li) - i - j == 100 and i != j:
            li.remove(i)
            li.remove(j)
li.sort()
for i in li:
    print(i)