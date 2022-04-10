# 영수증

# 10권의 총 가격
total = int(input())
 
# 10권의 총 가격에서 9권의 책의 가격을 1권씩 빼기
for i in range(9):
    book_price = int(input())
    total -= book_price

# 남은 1권의 가격 출력
print(total)