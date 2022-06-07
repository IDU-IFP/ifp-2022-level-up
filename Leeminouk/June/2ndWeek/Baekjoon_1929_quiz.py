# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 에라토스테네스의 채 미적용 4304ms 참고 소스로 수정
prime = {2: 0}
beside_prime = []
is_prime = True
start, end = map(int, input().split())

if start < 3:
    beside_prime.append(2)
    print(2)

for i in range(3, end + 1):
    for x in prime.keys():
        if x <= int(i ** .5):
            if i % x == 0:
                is_prime = False
                break
        
        else:
            break

    if is_prime:
        if i >= start:
            print(i)
        
        prime[i] = 0

    is_prime = True

# math.sqrt(n) == n ** .5

# 에라토스테네스의 채 적용 320ms < 참고함
# s, e = map(int, input().split())

# prime = [True] * (e + 1)
# s_e = int(e ** .5)
# for i in range(2, s_e + 1):
#     if prime[i]:
#         for x in range(i * i, e + 1, i):
#             prime[x] = False

# s = max(2, s)
# for p in range(s, e + 1):
#     if prime[p]:
#         print(p)
