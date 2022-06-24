def solution(x, y):
    if x < y:
        (x, y) = (y, x)
    # 유클리드 호재법

    def gcd(x, y):
        while(x % y != 0):
            (x, y) = (y, (x % y))
        return y
    # 최소 공배수 = 두 수의 곱 / 최대 공약수

    def lcm(x, y):
        return int((x * y) / gcd(x, y))
    answer = [gcd(x, y), lcm(x, y)]
    return answer
