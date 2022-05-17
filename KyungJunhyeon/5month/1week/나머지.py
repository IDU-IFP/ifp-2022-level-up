appendListNumber = []
recode = 0
count = 0
for _ in range(10):
    appendListNumber.append(int(input()) % 42)
print(len(set(appendListNumber)))
# 같은 원소를 합쳐주는 set 함수 사용
