#https://www.acmicpc.net/problem/2525

h,m = map(int,input().split())
plus_m = int(input())
sum_s = (h*3600) + ((m+plus_m)*60)  # 초 단위로 바꾸기

if sum_s >= 86400: 
    sum_s-=86400    # 24시 넘으면 0시로 변환
res_h = sum_s // 3600
res_m = sum_s % 3600 // 60
print(res_h,res_m)