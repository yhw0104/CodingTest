# 2주차 정리: 이진 탐색 & 재귀 함수

> 링크드 리스트 / 배열 비교는 [summary.md](summary.md) 참고.

| 주제 | 파일 | 시간복잡도 | 핵심 아이디어 |
|---|---|---|---|
| 순차 탐색 | `2_5_..._sequential.py` | O(N) | 앞에서부터 하나씩 확인 |
| 이진 탐색 | `2_6_..._binary.py` | O(log N) | 반씩 잘라내며 범위를 좁힌다 |
| 이진 탐색 응용 | `2_7`, `2_12` | O(N log N) | 정렬 후 이진 탐색 |
| 재귀 - 기본 | `2_8_count_down.py`, `2_9_factorial.py` | O(N) | 자기 자신을 더 작은 입력으로 호출 |
| 재귀 - 분할 | `2_10_is_palindrome.py` | O(N) | 양끝을 확인하고 안쪽으로 좁힌다 |
| 재귀 - DFS | `2_13_..._plus_or_minus.py` | O(2^N) | 모든 경우의 수를 가지치기로 탐색 |

---

# Part 1. 이진 탐색 (Binary Search)

## 1-1. 순차 탐색 vs 이진 탐색

```python
# 순차 탐색 - O(N)
for number in array:
    if target == number:
        return True
return False
```

- 정렬 여부와 무관하게 동작하지만, 최악의 경우 **N번** 비교.
- 원소가 100만 개면 100만 번 확인.

## 1-2. 이진 탐색

```python
def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1   # 오른쪽 절반만 남긴다
        else:
            current_max = current_guess - 1   # 왼쪽 절반만 남긴다
        current_guess = (current_min + current_max) // 2

    return False
```

### 어떻게 동작하나
> 전제: **배열이 반드시 정렬돼 있어야 한다.**

1. 탐색 범위의 **양 끝**(`min`, `max`)과 **중간**(`guess`)을 잡는다.
2. 중간값이 target이면 → 찾았다, 끝.
3. 중간값이 target보다 **작으면** → target은 오른쪽에 있다 → `min = guess + 1`
4. 중간값이 target보다 **크면** → target은 왼쪽에 있다 → `max = guess - 1`
5. 새 범위의 중간을 다시 잡고 반복.
6. `min > max`가 되면 범위가 사라진 것 → 없다, `False`.

### `target = 14`, `[1, 2, ..., 16]` 추적

| 회차 | min | max | guess | `array[guess]` | 판단 |
|---|---|---|---|---|---|
| 1 | 0 | 15 | 7 | `8` | `8 < 14` → 오른쪽으로 |
| 2 | 8 | 15 | 11 | `12` | `12 < 14` → 오른쪽으로 |
| 3 | 12 | 15 | 13 | `14` | **찾음 → True** |

16개짜리 배열을 **3번 만에** 끝냈다. 순차 탐색이면 14번.

### `target = 18` (없는 값) 추적

| 회차 | min | max | guess | `array[guess]` | 판단 |
|---|---|---|---|---|---|
| 1 | 0 | 15 | 7 | `8` | 오른쪽으로 |
| 2 | 8 | 15 | 11 | `12` | 오른쪽으로 |
| 3 | 12 | 15 | 13 | `14` | 오른쪽으로 |
| 4 | 14 | 15 | 14 | `15` | 오른쪽으로 |
| 5 | 15 | 15 | 15 | `16` | 오른쪽으로 |
| 6 | 16 | 15 | — | — | `min > max` → **False** |

### 왜 O(log N)인가

범위가 매번 **절반**으로 줄어든다.

```
16개 → 8개 → 4개 → 2개 → 1개   (4번)
N개를 몇 번 반으로 나눠야 1이 되는가 = log₂N
```

| N | 순차 탐색 | 이진 탐색 |
|---|---|---|
| 16 | 16회 | 4회 |
| 1,024 | 1,024회 | 10회 |
| 1,000,000 | 100만회 | **20회** |

## 1-3. 정렬되지 않은 입력에 쓰려면 (`2_7`, `2_12`)

이진 탐색의 전제는 정렬이므로, 입력이 섞여 있으면 **먼저 정렬**해야 한다.

```python
def is_available_to_order(menus, orders):
    menus.sort()                       # ← 전제 만들기 O(N log N)
    for order in orders:
        if binary_Check(menus, order) == False:
            return False
    return True
```

- 메뉴 N개, 주문 M개일 때: 정렬 `O(N log N)` + 탐색 `O(M log N)`
- 순차 탐색으로 했다면 `O(N × M)`.
- **주의**: 탐색을 딱 한 번만 할 거라면 정렬 비용(`N log N`)이 순차 탐색(`N`)보다 비싸다.
  **여러 번 반복 탐색할 때** 이득이 생긴다.
- 문자열도 사전순으로 비교 가능하므로 `"만두" < "오뎅"` 같은 비교가 그대로 동작한다.

---

# Part 2. 재귀 함수 (Recursion)

## 2-0. 재귀의 두 가지 필수 요소

```
1. 종료 조건 (base case)   — 더 이상 쪼갤 수 없는 가장 작은 경우
2. 점화식 (recursive case) — 자기 자신을 "더 작은 입력"으로 호출
```

둘 중 하나라도 빠지면 무한 재귀 → `RecursionError`.
Python의 기본 재귀 깊이 제한은 **약 1000**이다.

## 2-1. 카운트다운 (`2_8`)

```python
def count_down(number):
    print(number)
    if number == 0:
        return          # 종료 조건
    count_down(number - 1)   # 점화식: 입력이 1씩 작아진다
```

### 호출 흐름
```
count_down(3) → print(3)
  count_down(2) → print(2)
    count_down(1) → print(1)
      count_down(0) → print(0) → return  ← 종료
```

- 반환값 없이 **출력만** 하는 형태. 되돌아올 때 하는 일이 없다.

## 2-2. 팩토리얼 (`2_9`)

```python
def factorial(n):
    if n == 1:
        return 1              # 종료 조건
    return n * factorial(n-1) # 점화식: n! = n × (n-1)!
```

### 호출 흐름 — 내려갔다가 **올라오면서 계산**한다

```
factorial(5)
 = 5 * factorial(4)
     = 4 * factorial(3)
         = 3 * factorial(2)
             = 2 * factorial(1)
                 = 1          ← 여기서 되돌아가기 시작

되돌아오며 계산 ↑
2 * 1  = 2
3 * 2  = 6
4 * 6  = 24
5 * 24 = 120
```

- 카운트다운과 달리 **반환값을 받아서 쓴다**. 이게 재귀의 진짜 위력.

## 2-3. 회문 검사 (`2_10`)

```python
def is_palindrome(string):
    if len(string) <= 1:
        return True                    # 종료 조건
    if string[0] != string[-1]:
        return False                   # 양끝이 다르면 즉시 실패
    return is_palindrome(string[1:-1]) # 양끝을 떼고 안쪽만 검사
```

### 어떻게 동작하나
1. **양 끝 한 글자씩 비교** → 다르면 그 즉시 회문이 아니다.
2. 같으면 양 끝을 떼어내고 **가운데 문자열**에 대해 같은 질문을 반복.
3. 길이가 0 또는 1이 되면 더 볼 게 없으므로 회문.

### `"abcba"` 추적

| 호출 | 양끝 비교 | 다음 |
|---|---|---|
| `"abcba"` | `a` vs `a` ✓ | `"bcb"` |
| `"bcb"` | `b` vs `b` ✓ | `"c"` |
| `"c"` | 길이 1 | **True** |

> ⚠️ **종료 조건을 양끝 비교보다 먼저** 둬야 한다.
> `"abba"` 처럼 길이가 짝수면 `""`(빈 문자열)까지 줄어드는데,
> 이때 `string[0]`을 먼저 만지면 `IndexError`가 난다.

## 2-4. DFS로 모든 경우의 수 (`2_13`)

각 숫자 앞에 `+` 또는 `-`를 붙여 target을 만드는 방법의 수를 센다.

```python
def get_all_ways(array, current_index, current_sum):
    if current_index == len(array):    # 종료 조건: 끝까지 다 골랐다
        all_ways.append(current_sum)
        return

    get_all_ways(array, current_index + 1, current_sum + array[current_index])  # + 선택
    get_all_ways(array, current_index + 1, current_sum - array[current_index])  # - 선택

get_all_ways(array, 0, 0)
```

### 어떻게 동작하나
1. 현재 인덱스의 숫자에 대해 **`+`를 고른 경우로 끝까지 파고든다**.
2. 바닥(`current_index == len(array)`)에 닿으면 합을 기록하고 되돌아온다.
3. 되돌아온 지점에서 **`-`를 고른 경우로 다시 파고든다**.
4. 이렇게 모든 갈래를 다 훑는 것이 **DFS(깊이 우선 탐색)**.

### `[1, 1, 1]` 탐색 트리

```
                   sum=0  (index 0)
              +1  ↙        ↘  -1
           sum=1            sum=-1      (index 1)
        +1 ↙  ↘ -1        +1 ↙  ↘ -1
      2        0          0       -2    (index 2)
     ↙ ↘      ↙ ↘        ↙ ↘     ↙ ↘
    3   1    1  -1      1  -1   -1  -3  ← 바닥, 결과 기록
```

- 숫자 N개 각각 `+`/`-` 2가지 → 잎(leaf)이 **2^N개** → **O(2^N)**.
- `[1,1,1,1,1]`, target `3`이면 2^5 = 32가지 중 **5가지**가 정답.

### 재귀 파라미터 설계가 핵심

| 파라미터 | 역할 |
|---|---|
| `current_index` | 지금 몇 번째 숫자를 고를 차례인가 (진행 상황) |
| `current_sum` | 여기까지 고른 결과 (누적 상태) |

> 재귀는 **"지금 어디까지 왔는가"를 인자로 들고 다니는 것**이 전부다.
> 종료 조건은 보통 그 인자가 끝에 닿았을 때가 된다.

---

# 정리 한 줄

- **이진 탐색**: 정렬돼 있다는 전제 하나로 O(N) → O(log N). 100만 개를 20번에 끝낸다.
- **재귀**: 종료 조건 + 자기 자신을 더 작은 입력으로 호출. 반환값을 **받아서 쓰는지**(팩토리얼) 아닌지(카운트다운)를 구분할 것.
- **DFS**: 재귀로 모든 갈래를 훑는 것. 인자에 "현재 상태"를 담아 내려보낸다.
