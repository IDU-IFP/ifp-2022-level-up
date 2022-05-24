# 두 정수 A, B를 입력받고 A+B를 출력
"""
    입력 : 입력은 여러 테스트 케이스로 이루어짐
        각 테스트 케이스는 한 줄로 이루어져 있다
        각 줄에는 A, B가 주어짐 (0 < A, B < 10)
        입력의 마지막에는 0 두 개가 들어온다.
    출력 : 각 테스트 케이스마다 A + B를 출력함
"""
def testCase():
    numbers = []
    result = []

    while True:
        numbers = [int(a) for a in input().split()]

        if isEndNumber(numbers):
            break
        
        result.append(addAB(numbers))

    resultPrint(result)

def isEndNumber(numbers):
    return True if (numbers[0] == 0) and (numbers[1] == 0) else False

def addAB(numbers):
    return numbers[0] + numbers[1]

def resultPrint(numbers):
    
    for a in numbers:
        print(a)


testCase()