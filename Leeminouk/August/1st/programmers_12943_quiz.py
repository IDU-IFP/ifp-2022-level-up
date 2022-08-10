count = 0

def solution(num):
    global count
    if num != 1:
        count += 1

        if count >= 500:
            return -1
        else:
            if num % 2 == 0:
                return solution(int(num / 2))
            else:
                return solution((num * 3) + 1)

    else:
        return count

print(solution(int(input())))