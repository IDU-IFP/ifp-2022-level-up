# 세수정렬

# 정수를 입력받아 오름차순 정렬 후 차례대로 출력
print(*(sorted(list(map(int, input().split())))), sep=" ")