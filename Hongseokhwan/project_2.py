# 생일

n = int(input()) # 학생 수
name_list, day_list, month_list, year_list = [], [], [], [] # 이름, 일, 월, 년도를 담을 리스트
res = [] # 결과를 담을 리스트

# 학생 수만큼 반복
for i in range(n):
    # 이름, 일, 월, 년도 입력
    name, day, month, year = input().split(" ")

    # 맞는 리스트에 값 대입
    name_list.append(name)
    day_list.append(int(day))
    month_list.append(int(month))
    year_list.append(int(year))

    # 입력값들을 순차적으로 비교해 생일이 느린순으로 재배열
    for j in range(i):
        if(i > 0 and (year_list[i] > year_list[j] 
        or (year_list[i] == year_list[j] and month_list[i] > month_list[j]) 
        or (year_list[i] == year_list[j] and month_list[i] == month_list[j] and day_list[i] > day_list[j]))):

            temp_name = name_list[i]
            name_list[i] = name_list[j]
            name_list[j] = temp_name

            temp_day = day_list[i]
            day_list[i] = day_list[j]
            day_list[j] = temp_day

            temp_month = month_list[i]
            month_list[i] = month_list[j]
            month_list[j] = temp_month

            temp_year = year_list[i]
            year_list[i] = year_list[j]
            year_list[j] = temp_year

# 결과 리스트에 나이가 제일 적은 사람과 많은 사람만 추가
res.append(name_list[0])
res.append(name_list[n-1])

# 출력
for v in res:
    print(v)

