#https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    return list(map(int, str(n)[::-1]))
    # 1. n을 str형으로 변환 후 역순으로 정렬
    # 2. map 함수로 내용물을 int로 변환
    # 3. list 형태로 출력
