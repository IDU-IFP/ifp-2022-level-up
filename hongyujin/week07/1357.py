x, y = map(str, input().split())
sum = str(int(x[::-1]) + int(y[::-1]))  # 슬라이스를 이용해서 뒤집어준다
print(int(sum[::-1]))
