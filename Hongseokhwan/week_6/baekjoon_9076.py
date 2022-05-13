# 점수 집계

# 입력받은 테스트케이스 만큼 점수를 입력받아 총점인지 점수 조정(=KIN)인지 확인 후 출력
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))
    if(arr[3] - arr[1] >= 4):
        print("KIN")
    else:
        print(sum(arr[1:4]))