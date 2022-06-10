#https://www.acmicpc.net/problem/2941

# 처음 풀이방식
cro = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]

word = input()
count = len(word)
for i in range(len(word)-2):
    if word[i]+word[i+1]+word[i+2] == "dz=":
        count -= 1
for i in range(len(word)-1):
    if word[i]+word[i+1] in cro:
        count -= 1

print(count)

# 두번째 풀이 방식
cro = ["c=","c-","d-","lj","nj","s=","z=","dz="]

word = input()
count = len(word)

for c in cro:
    if c in word:
        count -= word.count(c)
        
print(count)