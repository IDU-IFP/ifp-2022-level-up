YUOT_PAIR = {0: "D", 1: "C", 2: "B", 3: "A", 4: "E"}

for _ in range(3):
    get_yout = list(map(int, input().split()))
    print(YUOT_PAIR[get_yout[0] + get_yout[1] + get_yout[2] + get_yout[3]])