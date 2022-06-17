# 12948번 핸드폰 번호 가리기 (프로그래머스)
def solution(phone_number):
    answer = []

    answer.append('*' * (len(phone_number)-4) + (phone_number[-4:]))
    return ''.join(answer)


phone_number = "01033334444"
print(solution(phone_number))