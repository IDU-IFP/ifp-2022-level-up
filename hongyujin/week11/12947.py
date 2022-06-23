def solution(x):
    sum = 0
    for i in str(x):  # 문자열로 바꿔줌
        sum += int(i)  # 자릿수를 더해준다
    if x % sum == 0:  # 하샤드 수 구하기
        return True
    else:
        return False
