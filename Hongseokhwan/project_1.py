# 첼시를 도와줘!

n = int(input()) # 테스트 케이스의 개수
res = [] # 결과를 담을 리스트

# 테스트 케이스만큼 반복
for i in range(n):
    p = int(input()) # 선수의 수

    # 선수의 정보를 담을 리스트
    price_list = []
    name_list=[]

    # 선수의 수만큼 반복
    for j in range(p):
        
        # 선수의 가격, 이름
        price, name = input().split(" ")
        price_list.append(int(price))
        name_list.append(name)
        
        # 가격 비교후 비싼 선수의 가격와 이름을 리스트의 우측으로 이동
        if(j > 0 and price_list[j] < price_list[j-1]):
            temp_price = price_list[j]
            price_list[j] = price_list[j-1]
            price_list[j-1] = temp_price

            temp_name = name_list[j]
            name_list[j] = name_list[j-1]
            name_list[j-1] = temp_name

    # 가장 우측에 있는 선수가 비싼 선수임으로 결과 리스트에 저장
    res.append(name_list[p-1]) 

# 결과 리스트에 있는 선수 이름 출력
for v in res:
    print(v)





