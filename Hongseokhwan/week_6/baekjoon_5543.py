# 상근날드

res_burger = 2000 # 세트버거의 최대가격 저장
res_drink = 2000 # 세트음료의 최대가격 저장

# 세트버거와 세트음료의 최소가격을 찾아 저장
for i in range(5):
    n = int(input())
    if(i < 3):
        if(res_burger > n):
            res_burger = n
    else:
        if(res_drink > n):
            res_drink = n

# 세트메뉴 가격 출력
print(res_burger + res_drink - 50)


