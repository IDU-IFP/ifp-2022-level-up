def logic(i):
    print({0: "E", 1: "A", 2: "B", 3: "C", 4: "D"}.get(i, "error"))


for _ in range(3):
    yout = list(map(int, input().split()))
    logic(yout.count(0))
