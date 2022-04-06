# 두 정수 A, B를 입력받은 다음, A + B를 출력하는 프로그램을 작성.
"""
    입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어짐.
        각 테스트 케이스는 한 줄로 이루어져 있고, 각 줄 A, B가 주어짐. (0 < A, B < 10)
    출력 : 각 테스트 케이스마다 A + B를 출력
"""
typed = int(input())

def testCase(typed):
    temp_add = []
    add_result = []
    
    for _ in range(typed):
        temp_add = [int(a) for a in input().split(" ")]
        add_result.append(addAB(temp_add))

    printResult(add_result)

def addAB(numbers):
    return numbers[0] + numbers[1]

def printResult(result):
    for a in result:
        print(a)

testCase(typed)