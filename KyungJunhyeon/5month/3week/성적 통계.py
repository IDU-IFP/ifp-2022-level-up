maxList = []
minList = []
Largest_GapList = []

num = int(input())

for _ in range(num):
    Largest_Gap = 0
    classList = list(map(int, input().split()))
    classList.sort(reverse=True)
    classList.pop()

    for i in range(len(classList)):
        if i != len(classList)-1:
            if classList[i] - classList[i+1] > Largest_Gap:
                Largest_Gap = classList[i] - classList[i+1]

    maxList.append(max(classList))
    minList.append(min(classList))
    Largest_GapList.append(Largest_Gap)

for i in range(num):
    print("Class", i+1)
    print("Max {}, Min {}, Largest gap {}".format(
        int(maxList[i]), int(minList[i]), int(Largest_GapList[i])))
