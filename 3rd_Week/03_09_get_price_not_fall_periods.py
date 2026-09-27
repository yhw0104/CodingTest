prices = [1, 2, 3, 2, 3]
from collections import deque


# for 문 활용
def get_price_not_fall_periods(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range (i+1, len(prices)):
            count = 0
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
   

    return answer
    
# Queue 활용 
# 앞에 데이터를 봅아오는데만 Queue를 사용함 그래서 Queue에 대한 이점 없음
# for문에서 사용하는 것과 같은 시간 복잡도를 가지고 있음
def get_price_not_fall_periods2(prices):
    result = []
    prices = deque(prices)

    while prices: #  prices가 비어있지 않다면 계속 반환한다. 비어있지 않다면 True, 비어있다면 False 반환
        price_not_fall_period = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price > next_price:
                price_not_fall_period += 1
                break
            price_not_fall_period += 1

        result.append(price_not_fall_period)

    return result

# print("for문 활용 정답")
# print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
# print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
# print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))

print("Queue 활용 정답")
print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods2(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods2([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods2([1, 5, 3, 6, 7, 6, 5]))