# 문제
# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# 입력
# 첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

# 출력
# 첫 줄에 구간에 속하는 숫자의 합을 출력한다.

sums_list = [int(a * (a + 1) / 2) for a in range(1, 46)]

start, end = map(int, input().split())

start_index, end_index = 0, 0

result = 0

for i in range(len(sums_list) - 1):
    if sums_list[i] <= start <= sums_list[i + 1]:
        start_index = i if sums_list[i] == start else i + 1

    if sums_list[i] <= end <= sums_list[i + 1]:
        end_index = i if sums_list[i] == end else i + 1

for i in range(start_index, end_index + 1):
    if start_index == end_index:
        result += (i + 1) * (end - start + 1)

    elif i == start_index:
        result += (start_index + 1) * (sums_list[i] - start + 1)

    else:
        if i == end_index:
            result += (end_index + 1) * (end_index + 1 - (sums_list[i] - end))

        else:
            result += (i + 1) ** 2

print(result)
