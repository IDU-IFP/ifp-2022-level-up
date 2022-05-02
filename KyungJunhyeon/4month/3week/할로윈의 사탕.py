# 할로윈데이에 한신이네는 아부지가 사탕을 나눠주신다. 
# 하지만 한신이의 형제들은 서로 사이가 좋지않아 서른이 넘어서도 사탕을 공정하게 나누어 주지 않으면 서로 싸움이 난다. 
# 매년 할로윈데이때마다 아부지는 사탕을 자식들에게 최대한 많은 사탕을 나누어 주시기 원하며 자신에게는 몇개가 남게되는지에 알고 싶어 하신다. 
# 이런 아부지를 도와서 형제간의 싸움을 막아보자.
testCase = int(input())
getCandy = []
dadCandy = []
for _ in range(testCase):
    candy, bro = map(int, input().split())
    getCandy.append(int(candy/bro))
    dadCandy.append(int(candy%bro))
for i in range(testCase):
    print("You get",getCandy[i],"piece(s) and your dad gets",dadCandy[i],"piece(s).")