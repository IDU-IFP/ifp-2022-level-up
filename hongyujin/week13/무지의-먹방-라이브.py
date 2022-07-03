from operator import itemgetter
import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간 보다 k가 크거나 같으면 -1을 반환
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐 이용
    q = []
    for i in range(len(food_times)):
        # 음식 시간, 음식 번호 형태로 우선 순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간

    length = len(food_times)  # 남은 음식의 개수

    # (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1  # 다 먹은 음식 시간 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

# ===============================================


def solution(food_times, k):
    foods = []
    n = len(food_times)  # 음식의 개수
    for i in range(n):
        # 투플 형태로 처음 값 = 음식 시간, 두 번째 값 = 음식 번호
        foods.append((food_times[i], i + 1))

    foods.sort()  # 첫 번째 값을 음식 시간으로 (음식순) 오름차순 정렬

    pretime = 0  # 이전 음식을 먹은데 필요한 시간
    for i, food in enumerate(foods):
        # 음식을 먹는데 필요한 시간 - 이전 음식을 먹는데 필요한 시간 (정렬하면 처음에 1이여서 그냥 쓴다)
        diff = food[0] - pretime
        if diff != 0:  # diff가 0이 아니면 소비한 시간 구해서 뺄 수 있음
            spend = diff * n  # 소비한 시간 = diff * 남은 음식의 개수
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                # 남은 음식 음식 번호로 정렬
                sublist = sorted(foods[i:], key=itemgetter(1))
                return sublist[k][1]  # 그 음식의 번호를 반환해야 하니가 인덱스 1을 써야한다
        n -= 1  # 턴이 끝날때마다 음식 하나를 먹은거기 때문에 -1 해준다

    return -1  # 더 섭튀할 음식이 없으면 -1을 반환
