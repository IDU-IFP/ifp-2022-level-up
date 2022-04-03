    # 어떤 반의 학생 생일 중 가장 나이가 적은 사람과 가장 나이가 많은 사람
"""
    입력 : 첫 줄은 반에 있는 학생 수 n (1 <= n <= 100)
    
    다음 n개의 줄 각 학생의 이름, 생일 '이름 dd mm yyyy' 이름 < 15글자
    dd mm yyyy 는 생일의 일, 월, 연도 (1990 <= yyyy <= 2010, 1 <= mm <= 12, 1 <= dd <= 31)
        단 날짜의 오입력은 없음, 연, 월, 일은 0으로 시작하지 않음
        이름과 생일이 같은 사람은 없음

    출력 : 첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름 출력
"""

total_birth = []


def getStudentTotal(max_student):
    total_student = []
    total = int(max_student)

    for _ in range(total):
        total_student.append(input())

    return total_student

def findOldestStudent(total_student):
    splited = studentBirthSplit(total_student)
    temp_name = ""
    temp_birth = None

    for key, val in splited.items():
        if temp_birth:
            temp_birth = birthDay(temp_birth)
            val_birth = birthDay(val)

            if val_birth[0] < temp_birth[0]:
                temp_birth = val
                temp_name = key

            elif val_birth[0] == temp_birth[0]:
                if val_birth[1] < temp_birth[1]:
                    temp_birth = val
                    temp_name = key

                elif val_birth[1] == temp_birth[1]:
                    if val_birth[2] < temp_birth[2]:
                        temp_birth = val
                        temp_name = key

        else:
            temp_name = key
            temp_birth = val

    return temp_name

def findYoungestStudent(total_student):
    splited = studentBirthSplit(total_student)
    temp_name = ""
    temp_birth = None

    for key, val in splited.items():
        if temp_birth:
            temp_birth = birthDay(temp_birth)
            val_birth = birthDay(val)

            if val_birth[0] > temp_birth[0]:
                temp_birth = val
                temp_name = key

            elif val_birth[0] == temp_birth[0]:
                if val_birth[1] > temp_birth[1]:
                    temp_birth = val
                    temp_name = key

                elif val_birth[1] == temp_birth[1]:
                    if val_birth[2] > temp_birth[2]:
                        temp_birth = val
                        temp_name = key

        else:
            temp_name = key
            temp_birth = val

    return temp_name

def studentBirthSplit(total_student):
    splited = dict()
    temp_dict = dict()
    temp_name = ""
    temp = []

    for x in total_student:
        splited_student_info = x.split(" ")

        for a, b in enumerate(splited_student_info):

            if a < 1:
                temp_name = b

            elif a == 1:
                temp.append(b)
            
            else:
                temp.append(b + " ")

        temp.reverse()
        temp_dict = {temp_name: temp}
        splited.update(temp_dict)

        temp = []

    return splited

def birthDay(birth):
    temp = []
    
    for x in birth:
        temp.append(int(x))

    return temp


while True:
    how_many_people = input()

    if how_many_people:
        total_student = getStudentTotal(how_many_people)
        print(findYoungestStudent(total_student))
        print(findOldestStudent(total_student))
        break

    else:
        print("value error or no value")
        break