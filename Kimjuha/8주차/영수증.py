total = int(input())
book = []
for i in range(9):
    book.append(int(input()))
print(total-sum(book))
