k,e,m,s=map(int,input().split())

if not (0 <= k <= 100 and 0 <= e <= 100 and 0 <= m <= 100 and 0 <= s <= 100):
    print('잘못된 점수')
else:
    average=(k+e+m+s)/4

    if average>=80:
        print("합격")
    else:
        print("불합격")