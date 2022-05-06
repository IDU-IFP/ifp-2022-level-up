# 구단에서 가장 비싼 선수를 확인하고 영입하기
"""
    입력 : n (n <= 100)

    1번 줄 p = 고려해야할 선수 수 (1 <= p <= 100)
    그외 줄 p개 : 선수 정보 표시
    각각 줄은 선수 가격 c 와 이름 입력 (c < 2*10^9)
        단 모든 선수의 가격은 다름
        선수의 이름은 20자 이하, 사이에 공백은 없음

    출력 : 각각 테스트 케이스별 가장 비싼 선수 출력
"""

testcase = ["""
            2
            3
            10 Iversen
            1000000 Nannskog
            2000000 Ronaldinho
            2
            1000000 Maradona
            999999 Batistuta
            """ ]

total_member_info = []


def memberPrice(total):
    total_group_count = int(total)
    total_info = []
    temp_info = []

    for _ in range(total_group_count):
        how_many_people = input()
        total_group = int(how_many_people)

        for _ in range(total_group):
            temp_info.append(input())

        total_info.append(temp_info)
        temp_info = []

    return total_info

def expensiveMember(total_member_info):
    member_group_by = memberGroupBy(total_member_info)
    expensive_members = []
    temp_key = ""
    temp_val = 0

    for x in member_group_by:

        for key, val in x.items():
            if temp_val < val:
                temp_key = key
                temp_val = val
        
        expensive_members.append(temp_key)

        temp_key = ""
        temp_val = 0

    return expensive_members

def memberGroupBy(total_member_info):
    splited_member = []

    for a in total_member_info:
        splited = inputSplit(total_member_info, len(a), total_member_info.index(a))
        splited_member.append(splited)

    return splited_member

def inputSplit(total_member_info, group_max, position):
    sliced_member = dict()

    for x in range(group_max):
        get_member = str(total_member_info[position][x])
        splited = get_member.split(" ")
        sliced_member.update({splited[1]: int(splited[0])})

    return sliced_member


while True:
    how_much_ask = input()

    total_member_info = memberPrice(how_much_ask)

    if total_member_info:
        result = expensiveMember(total_member_info)

        for a in result:
            print(f"{a}")
        break

    else:
        print("no value called")
        break