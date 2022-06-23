import math
hour, min = map(int, input().split())
plusMin = int(input())

if plusMin+min < 60:
    min = plusMin+min
else:
    hour += math.floor((plusMin+min) / 60)
    min = (plusMin+min) % 60

if hour >= 24:
    hour -= 24

print(hour, min)
