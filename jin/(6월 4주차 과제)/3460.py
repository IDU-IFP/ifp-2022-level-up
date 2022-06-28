TEST = int(input())

for i in range(TEST):
    NUM = int(input())
    NUM = format(NUM, 'b')
    S = list(map(int, str(NUM)))
    S.reverse()
    for j in range(len(S)):
        if S[j] == 1:
            print(j, end = ' ')