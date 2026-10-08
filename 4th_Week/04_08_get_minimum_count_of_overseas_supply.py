# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
# 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies),
# 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.
# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.
import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0                      # 받은 횟수
    last_added_date_index = 0       #다음에 후보로 넣을 공급 날짜
    max_heap = []                   # 후보목록(가장 큰걸 빨리 꺼내려고 힙 사용)

    while stock < k:                # 아직 k일까지 못버티면 계속
        # 내 재고로 버티는 날까지 도착하는 공급을 전부 후보에 넣기
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        # 후보중 가장 큰 것 하나를 받기
        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))

# 경계값 테스트 케이스들

# 1. stock = k (이미 충분한 경우)
print("정답 = 0 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [5], [20], 10))

# 2. stock = 0 (재고 완전 바닥)
print("정답 = 2 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 10, 15], [20, 10, 15], 35))

# 3. 딱 한 번만 공급받으면 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5], [30], 30))

# 4. 공급 후 stock이 정확히 k가 되는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10], [20], 30))

# 5. 첫날부터 공급 가능한 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [100], 50))

# 6. k = 1 (최소 기간)
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0], [10], 1))

# 7. 여러 번 공급받아야 하고 딱 맞아떨어지는 경우
print("정답 = 3 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(0, [0, 5, 10], [5, 5, 5], 15))

# 8. 공급 가능 날짜가 여러 개지만 하나만 선택해야 하는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(5, [5, 6, 7], [100, 10, 10], 50))

# 9. 마지막 날에 공급받는 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(10, [10, 29], [20, 100], 30))

# 10. stock이 k보다 1 작은 경우
print("정답 = 1 / 현재 풀이 값 =", get_minimum_count_of_overseas_supply(29, [29], [100], 30))