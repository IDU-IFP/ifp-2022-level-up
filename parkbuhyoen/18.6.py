start, stop = map(int, input().split())
 
i = start
 
while True:
    remain=i%10
    if i>stop:
        break
    if remain==3:
        i += 1
        continue
    else:
        print(i, end=' ')
        i += 1