word=input()
case=len(word)//10
last=len(word)%10
for i in range (case):
    print(word[i*10:i*10+10])
if last!=0:
    print(word[-last:])