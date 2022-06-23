a, b = map(int, input().split())
c = int(input())

hour = (a + (b + c) // 60) % 24  # % 24는 24시가 넘어갔을 때 0시로 바꿔준다
minute = (b + c) % 60
print(hour, minute)
