# 백설 공주와 일곱 난쟁이

arr = [] # 정수를 담을 배열

# 9개의 정수를 입력
for _ in range(9):
    arr.append(int(input()))

# 임의의 두 수를 뽑아 총합에서 두 수의 합을 뺐을 때 100이 되면 
# 두 수를 제외 한 후 반복문 탈출
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        a = arr[i]
        b = arr[j]

        if(sum(arr) - (a+b) == 100):
            arr.remove(a)
            arr.remove(b)
            break
        
    if(len(arr) == 7):
        break

 # 일곱난쟁이 출력
print(*arr, sep="\n")