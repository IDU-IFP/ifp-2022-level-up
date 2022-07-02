# 오븐 시계

h, m = map(int, input().split()) # 현재 시간
t = int(input()) # 걸리는 시간

res_m = (m+t) % 60 # 분끼리 더해 60 으로 나눈 나머지가 최종 분
res_h = (h+((m+t)//60)) % 24 # 시에 분끼리 더한 몫을 더해 24 로 나눈 나머지가 최종 시

# 시와 분 출력
print(res_h, res_m)