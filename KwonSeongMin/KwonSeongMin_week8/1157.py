#https://www.acmicpc.net/problem/1157

al = [0 for _ in range(26)] # a~z
l = input().lower()
m = 0
print_al = 0
flag = 0
for i in l:
    al[ord(i)-97] += 1  # 단어 저장

for i in range(26):
    if al[i] > m:   #단어 개수가 많아지면
        flag = 0    
        m = al[i]
        print_al = 65 + i
        al[i] = 0;
    if al[i] == m:
        flag = 1    # 단어가 겹쳤을 때
        
if(flag):
    print("?")
    quit()
else:
    print(chr(print_al))