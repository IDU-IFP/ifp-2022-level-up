def soultion(phone_number):
    answer = ''  # *로 가린 정답을 저장할 변수
    phone_len = len(phone_number)  # phone_number의 길이 저장 변수
    answer += '*' * (phone_len - 4) + phone_number[-4:]  # 길이에서 -4만큼 *을 넣는다
    return answer
