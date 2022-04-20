# 영수증

# 10권의 총 가격 입력
money = int(input())

# 9권의 책의 가격을 순차적으로 입력하여 10권의 총 가격에서 빼기
for i in range(9):
    price = int(input()) 
    money -= price # 

# 가격을 읽을 수 없는 책의 가격 출력
print(money)