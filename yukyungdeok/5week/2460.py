# 2460번 지능형 기차 2
people = 0
max_people = 0

for _ in range(10):
    people_out, people_in = map(int, input().split())
    people += people_in - people_out
    max_people = max(people, max_people)
print(max_people)