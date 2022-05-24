# 성적 통계

# 테스트 케이스만큼 반복
# 학생 수를 제외한 나머지 값을 오름차순으로 정렬해 최대 차이를 구한 후 최대값, 최소값, 최대차이 출력
for i in range(int(input())):
    class_arr = sorted(list(map(int, input().split()))[1:])
    gap = 0
    for j in range(len(class_arr)-1):
        if(class_arr[j+1]-class_arr[j] > gap):
            gap = class_arr[j+1]-class_arr[j]

    print("Class",i+1)
    print("Max {}, Min {}, Largest gap {}".format(class_arr[-1], class_arr[0], gap))