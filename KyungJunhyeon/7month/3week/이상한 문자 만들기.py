'''
def strToOrd(listName):
    tempList = []
    for i in listName:
        tempList.append(ord(i))
    return tempList


def ordToStr(listName):
    tempList = []
    for i in listName:
        tempList.append(chr(i))
    return tempList


def ordToOdd(listName):
    finalList = []
    flg = 0
    for i in listName:
        if flg == 0:
            if i < 96:
                finalList.append(i)
            else:
                finalList.append(i-32)
            flg = 1
        else:
            if i < 96:
                finalList.append(i+32)
            else:
                finalList.append(i)
            flg = 0
    return finalList


def joinList(listName):
    string = "".join(listName)
    return string


def solution(s):
    strlist = list(map(str, s.split()))
    ordTemp = []
    chrTemp = []
    finalTemp = []
    for word in strlist:
        ordTemp = strToOrd(word)
        ordTemp = ordToOdd(ordTemp)
        chrTemp = ordToStr(ordTemp)
        finalTemp.append(joinList(chrTemp))

    answer = " ".join(finalTemp)
    return answer


print(solution(input()))


이게 왜 안되는건지 반례를 찾고싶은데 못찾겠네요
'''


def toWeirdCase(s):
    res = []
    for x in s.split(' '):
        word = ''
        for i in range(len(x)):
            c = x[i].upper() if i % 2 == 0 else x[i].lower()
            word = word + c
        res.append(word)
    return ' '.join(res)


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(toWeirdCase("try hello world")))
