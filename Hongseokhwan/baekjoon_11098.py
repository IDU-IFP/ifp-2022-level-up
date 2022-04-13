n = int(input()) # 테스트 케이스의 개수
res = [] # 결과를 담을 리스트

# 테스트 케이스만큼 반복
for i in range(n):
    p = int(input()) # 선수의 수

    # 선수의 정보
    price_list = []
    name_list=[]

    for j in range(p):
        price, name = input().split(" ")
        price_list.append(int(price))
        name_list.append(name)
        
        if(j > 0 and price_list[j] < price_list[j-1]):
            temp_price = price_list[j]
            price_list[j] = price_list[j-1]
            price_list[j-1] = temp_price

            temp_name = name_list[j]
            name_list[j] = name_list[j-1]
            name_list[j-1] = temp_name

            

    res.append(name_list[p-1]) 
for v in res:
    print(v)





