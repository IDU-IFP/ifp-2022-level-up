def sosu(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


sosu_list = []

while True:
    sosu_list.clear()
    n = int(input())
    if n == 0:
        break

    if n == 1:
        print(1)

    if n > 1:
        for i in range(n + 1, 2 * n):
            if sosu(i):
                sosu_list.append(i)
        print(len(sosu_list))
