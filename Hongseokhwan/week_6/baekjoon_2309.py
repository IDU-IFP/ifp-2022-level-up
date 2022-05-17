# 일곱 난쟁이

arr = [] # 난쟁이의 키를 담을 배열

# 난쟁이의 키 입력
for _ in range(9):
    arr.append(int(input()))

# 임의의 두 난쟁이의 키를 총합에서 뻈을 때 100이 나오면 
# 두 난쟁이의 키를 제거 후 반복문 탈출
for i in range(8):
    for j in range(i+1,9):
        if(sum(arr) - (arr[i] + arr[j]) == 100):
            f_num, s_num = arr[i], arr[j]
            arr.remove(f_num)
            arr.remove(s_num)
            break
    
    if(len(arr) == 7):
        break

# 오름차순 정렬 후 출력
print(*(sorted(arr)), sep="\n")