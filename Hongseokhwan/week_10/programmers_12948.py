# 핸드폰 번호 가리기

def solution(phone_number):
    # 전화번호 뒷 4자리 제외한 나머지를 *로 표기
    return "*" * (len(phone_number)-4) + phone_number[-4:]