# N을 입력받으면 구구단의 N단을 출력
"""
    입력 : 첫째 줄은 N이 주어짐 (1 <= N <= 9)
    출력 : 출력 형식과 같게 N * 1 ~ N * 9 까지 출력
"""
typed = int(input())

goo_num = 10
multi = 0
for a in range(1, goo_num):
    multi = a * typed
    print(f"{typed} * {a} = {multi}")
