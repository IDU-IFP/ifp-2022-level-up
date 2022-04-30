# 10부제

date = input() # 날짜의 일의 숫자 입력
car_num = input().split(" ") # 5대의 자동차 번호의 일의 숫자 입력

# 자동차 번호의 일의 숫자가 날짜의 일의 숫자와 동일한 자동차 카운트
res = car_num.count(date) 

# 출력
print(res)