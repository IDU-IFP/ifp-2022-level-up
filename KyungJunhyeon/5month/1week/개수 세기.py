# listNum = [0 for i in range(int(input()))] 양식미를 위해 존재하는 쓸모없는 구간, 이걸 쓸모있게 하려면 도대체 어떻게 코드를 짜야하지?
int(input())  # 이걸로 충분하긴 함.
listNum = list(map(int, input().split()))
print(listNum.count(int(input())))
