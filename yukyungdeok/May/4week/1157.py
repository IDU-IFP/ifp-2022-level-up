# 1157번 단어 공부
w = input().lower()
w_list = list(set(w))
count_w = []

for i in w_list:
    count = w.count(i)
    count_w.append(count)
    
if count_w.count(max(count_w)) >= 2:
    print("?")
else:
    print(w_list[(count_w.index(max(count_w)))].upper())