people = 0
max_people = 0

for _ in range(10):
    out_people, in_people = map(int, input().split())
    people += in_people - out_people
    max_people = max(people, max_people)

print(max_people)
