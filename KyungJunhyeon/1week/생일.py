# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

peopleNumber = int(input())
defaultOldYear = 0

for i in range(peopleNumber):
    name, day, month, year = input().split()

    day = int(day)
    month = int(month)
    year = int(year)

    # init
    if defaultOldYear == 0:
        defaultOldYear = year
        defaultOldMonth = month
        defaultOldDay = day
        oldMansName = name

        defaultYoungYear = year
        defaultYoungMonth = month
        defaultYoungDay = day
        youngMansName = name

    # Old People
    if (defaultOldYear != 0 and (defaultOldYear > year)):
        defaultOldYear = year
        defaultOldMonth = month
        defaultOldDay = day
        oldMansName = name
    elif (defaultOldYear != 0 and (defaultOldYear == year)):
        if (defaultOldMonth > month):
            defaultOldYear = year
            defaultOldMonth = month
            defaultOldDay = day
            oldMansName = name
        elif (defaultOldMonth == month):
            if (defaultOldDay > day):
                defaultOldYear = year
                defaultOldMonth = month
                defaultOldDay = day
                oldMansName = name

    # Young People
    if (defaultYoungYear != 0 and (defaultYoungYear < year)):
        defaultYoungYear = year
        defaultYoungMonth = month
        defaultYoungDay = day
        youngMansName = name
    elif (defaultYoungYear != 0 and (defaultYoungYear == year)):
        if (defaultYoungMonth < month):
            defaultYoungYear = year
            defaultYoungMonth = month
            defaultYoungDay = day
            youngMansName = name
        elif (defaultYoungMonth == month):
            if (defaultYoungDay < day):
                defaultYoungYear = year
                defaultYoungMonth = month
                defaultYoungDay = day
                youngMansName = name

print(oldMansName)
print(youngMansName)
