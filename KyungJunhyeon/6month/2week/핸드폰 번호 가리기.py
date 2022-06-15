def solution(phone_number):
    phoneList = list(phone_number)
    for i in range(len(phoneList[:-4])):
        phoneList[i] = "*"
    answer = "".join(phoneList)
    return answer