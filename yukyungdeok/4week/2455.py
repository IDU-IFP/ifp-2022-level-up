# 2455번 지능형 기차

people_nums = []
people = 0

for _ in range(4):
    people_out, people_in = map(int, input().split())
    people += people_in
    people -= people_out
    
    people_nums.append(people)
    
print(max(people_nums))