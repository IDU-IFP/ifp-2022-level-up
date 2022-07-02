burger=[]
for i in range (5):
    burger.append(int(input()))

print(min(burger[:3])+min(burger[3:])-50)