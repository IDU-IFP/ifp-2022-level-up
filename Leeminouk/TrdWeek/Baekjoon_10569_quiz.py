# 수학자가 구를 깎아서 볼록 다면체를 만들었다. 이 임의의 볼록 다면체는 꼭짓점 수 - 모서리 수 + 면의 수 = 2 면의 수는 세지 않음
"""
    입력 : 첫째 줄에는 T (1 <= T <= 100)
            다음 T개의 줄에는 V, E (4 <= V, E <= 100) 
            V : 꼭짓점 개수, E : 모서리 개수
    출력 : V, E에 볼록 다면체의 면 수를 한 줄에 하나씩 출력
    식 : 면의 수 = 2 - V + E
"""
import sys
typed = int(sys.stdin.readline())

for _ in range(typed):
    v, e = [int(a) for a in sys.stdin.readline().split()]
    print(e - v + 2)