# 2개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램
"""
    입력 : 첫째 줄에는 두 개의 자연수. (<= 10000)
        자연수, 사이의 1칸 공백
    출력 : 첫째 줄에는 두 수의 최대 공약수, 둘째 줄에는 최소 공배수
"""
# 최대공약수, 최소공배수 알고리즘 참조
def getGCDandLCM():
    typed = input()
    numbers = splitNumber(typed)
    print(theGCD(numbers))
    print(theLCM(numbers))

def splitNumber(typed):
    return toIntChanger(typed.split(" "))

def toIntChanger(numbers):
    return [int(number) for number in numbers]

def theGCD(numbers):    # the Greatest Common Denominator 최대공약수
    num_one = numbers[0]
    num_two = numbers[1]
    result = 0

    while True:
        result = num_one % num_two

        if result == 0:
            return num_two
        
        else:
            num_one, num_two = num_two, result

def theGCDRe(num_one, num_two):    # the Greatest Common Denominator 최대공약수 재귀함수
    result = num_one % num_two
    return num_two if result == 0 else theGCDRe(num_two, result)

def theLCM(numbers):    # the Least Common Multiple 최소공배수
    gcd = theGCDRe(numbers[0], numbers[1])
    result = numbers[0] * int(numbers[1] / gcd)
    return result

getGCDandLCM()