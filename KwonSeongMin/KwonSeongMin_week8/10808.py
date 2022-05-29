#https://www.acmicpc.net/problem/10808

al = [0 for _ in range(26)] # a~z
l = input()

for i in l:
    al[ord(i)-97] += 1  # 단어 저장

for j in al:
    print(j,end=" ")