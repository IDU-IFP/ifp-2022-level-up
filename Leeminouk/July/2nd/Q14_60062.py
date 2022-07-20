from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    weak += [(n + a) for a in weak]
    answer = 9

    for i in range(weak_len):
        for set in list(permutations(dist, len(dist))):
            count = 1
            pos = weak[i] + set[count - 1]

            for j in range(i, i + weak_len):
                if pos < weak[j]:
                    count += 1
                    if count > len(dist):
                        break
                    pos = weak[j] + set[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer

# print(list(permutations({1, 2, 3, 4, 5, 6, 7, 8, 9}, 3)))