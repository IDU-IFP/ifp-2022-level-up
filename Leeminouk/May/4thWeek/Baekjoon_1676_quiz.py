# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

number = int(input())
zero_count = 0

def factorial(n):    
    return factorial(n - 1) * n if n > 1 else 1

for a in str(factorial(number))[::-1]:
    if a == "0":
        zero_count += 1
        
    else:
        break

print(zero_count)