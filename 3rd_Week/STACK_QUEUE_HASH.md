# 3주차 스택 · 큐 · 해시 정리

| 자료구조 | 파일 | 핵심 규칙 | 넣기 / 빼기 |
|---|---|---|---|
| 스택 | `03_06_stack.py` | **LIFO** (나중에 넣은 게 먼저 나온다) | O(1) / O(1) |
| 큐 | `03_08_queue.py` | **FIFO** (먼저 넣은 게 먼저 나온다) | O(1) / O(1) |
| 해시 테이블 | `03_10_dict.py`, `03_10_dict_chaining.py` | key를 **해시 함수로 인덱스로 바꿔** 바로 접근 | 평균 O(1) / 평균 O(1) |

| 문제 | 파일 | 사용한 아이디어 |
|---|---|---|
| 탑 레이저 신호 | `03_07_get_receiver_top_orders.py` | 스택처럼 뒤에서부터 `pop` 하며 왼쪽 탐색 |
| 주식 가격 | `03_09_get_price_not_fall_periods.py` | 큐처럼 앞에서부터 `popleft` 하며 오른쪽 탐색 |

---

## 1. 스택 (Stack)

```python
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head   # 새 노드가 기존 head를 가리키고
        self.head = new_head        # head를 새 노드로 교체

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        delete_head = self.head
        self.head = self.head.next  # head를 한 칸 뒤로
        return delete_head

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None
```

### 어떻게 동작하나
- 접시 쌓기와 같다. **맨 위(`head`)에서만 넣고 뺀다.**
- `push`: 새 노드를 맨 위에 올리고, 새 노드가 이전 맨 위를 가리키게 한다.
- `pop`: 맨 위 노드를 떼어내고, `head`를 그 아래 노드로 옮긴다.
- `peek`: 빼지 않고 맨 위 값만 본다.
- 링크드 리스트의 **맨 앞만 건드리므로** 전부 O(1).

### `push(4) → push(3) → push(5) → pop() × 3` 추적

| 연산 | 스택 상태 (왼쪽이 top) | peek |
|---|---|---|
| `push(4)` | `[4]` | `4` |
| `push(3)` | `[3, 4]` | `3` |
| `push(5)` | `[5, 3, 4]` | `5` |
| `pop()` | `[3, 4]` | `3` |
| `pop()` | `[4]` | `4` |
| `pop()` | `[]` | `stack is empty` |

> 파이썬에서는 그냥 `list`를 스택으로 쓴다. `append()`가 push, `pop()`이 pop, `[-1]`이 peek. 모두 O(1).

### 언제 쓰나
- **가장 최근 것부터** 처리해야 할 때: 괄호 짝 맞추기, 되돌리기(Ctrl+Z), 웹 브라우저 뒤로 가기
- 재귀 함수 호출도 내부적으로 **콜 스택**에 쌓인다. (2주차 재귀와 연결)

## 2. 문제: 탑 레이저 신호 (`03_07`)

> 각 탑이 **왼쪽으로** 신호를 쏜다. 자기보다 **높거나 같은** 탑 중 가장 가까운 탑이 받는다. 받은 탑의 번호(1부터)를 기록, 없으면 0.

```python
def get_receiver_top_orders2(heights):
    answer = [0] * len(heights)
    while heights:
        height = heights.pop()                       # 맨 오른쪽 탑을 꺼낸다
        for idx in range(len(heights) - 1, -1, -1):  # 남은 탑을 오른쪽→왼쪽으로
            if height <= heights[idx]:
                answer[len(heights)] = idx + 1       # pop 후 길이 = 꺼낸 탑의 인덱스
                break
    return answer
```

### 풀이 흐름
1. **맨 오른쪽 탑부터 `pop`** 한다. (스택처럼 뒤에서 꺼냄)
2. 남아 있는 탑들은 전부 꺼낸 탑의 **왼쪽**에 있는 탑들이다.
3. 그 중 가장 가까운 것부터(= 뒤에서부터) 보면서 나보다 높거나 같은 탑을 찾으면 기록하고 `break`.
4. `pop` 하고 난 뒤의 `len(heights)`가 곧 **꺼낸 탑의 원래 인덱스**라는 점이 포인트.

### `[6, 9, 5, 7, 4]` 추적

| 꺼낸 탑 | 남은 탑 | 왼쪽으로 탐색 | 결과 |
|---|---|---|---|
| `4` (idx 4) | `[6, 9, 5, 7]` | `7 ≥ 4` ✓ | `answer[4] = 4` |
| `7` (idx 3) | `[6, 9, 5]` | `5` X, `9 ≥ 7` ✓ | `answer[3] = 2` |
| `5` (idx 2) | `[6, 9]` | `9 ≥ 5` ✓ | `answer[2] = 2` |
| `9` (idx 1) | `[6]` | `6` X | `answer[1] = 0` |
| `6` (idx 0) | `[]` | 없음 | `answer[0] = 0` |

→ `[0, 0, 2, 2, 4]`

- 이중 반복이라 **O(N²)**. (스택에 "아직 신호를 받을 수 있는 후보 탑"만 남겨두는 방식으로 O(N)까지 줄일 수 있다.)

## 3. 큐 (Queue)

```python
class Queue:
    def __init__(self):
        self.head = None   # 빼는 쪽 (앞)
        self.tail = None   # 넣는 쪽 (뒤)

    def enqueue(self, value):
        # 새 노드를 tail 뒤에 붙이고, tail을 새 노드로 옮긴다
        ...

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeue = self.head.data
        self.head = self.head.next   # head를 한 칸 뒤로
        return dequeue
```

### 어떻게 동작하나
- 줄 서기와 같다. **뒤(`tail`)로 들어오고, 앞(`head`)으로 나간다.**
- 스택과 달리 양쪽 끝을 다 쓰기 때문에 **포인터가 `head`, `tail` 두 개** 필요하다.
  - `tail`이 없으면 넣을 때마다 끝까지 따라가야 해서 O(N)이 된다.
- `enqueue`: `tail.next = 새 노드` → `tail = 새 노드`
- `dequeue`: `head` 값을 꺼내고 `head = head.next`
- **비어 있을 때** 첫 노드를 넣으면 `head`와 `tail`이 **같은 노드**를 가리켜야 한다. (예외 처리 필요)

### `enqueue(4, 2, 3, 7) → dequeue() × 3` 추적

| 연산 | 큐 상태 (왼쪽이 head) | peek |
|---|---|---|
| `enqueue(4)` | `[4]` | `4` |
| `enqueue(2)` | `[4, 2]` | `4` |
| `enqueue(3)` | `[4, 2, 3]` | `4` |
| `enqueue(7)` | `[4, 2, 3, 7]` | `4` |
| `dequeue()` → `4` | `[2, 3, 7]` | `2` |
| `dequeue()` → `2` | `[3, 7]` | `3` |
| `dequeue()` → `3` | `[7]` | `7` |

> 파이썬에서는 `collections.deque`를 큐로 쓴다. `append()`로 넣고 `popleft()`로 뺀다. 둘 다 O(1).
> ⚠️ `list.pop(0)`은 뒤 원소를 전부 한 칸씩 당겨야 해서 **O(N)** 이다.

### 언제 쓰나
- **들어온 순서대로** 처리해야 할 때: 작업 대기열, 프린터 출력, BFS(너비 우선 탐색)

## 4. 문제: 주식 가격 (`03_09`)

> 각 시점의 가격이 **떨어지지 않은 기간**이 몇 초인지 구한다. 떨어진 순간도 1초로 센다.

```python
def get_price_not_fall_periods2(prices):
    result = []
    prices = deque(prices)

    while prices:
        price_not_fall_period = 0
        current_price = prices.popleft()   # 맨 앞 가격을 꺼낸다
        for next_price in prices:          # 남은 가격 = 이후 시점들
            if current_price > next_price:
                price_not_fall_period += 1 # 떨어진 순간도 1초로 센다
                break
            price_not_fall_period += 1
        result.append(price_not_fall_period)
    return result
```

### 풀이 흐름
1. **맨 앞 가격을 `popleft`** 한다. (큐처럼 앞에서 꺼냄)
2. 남아 있는 가격들은 전부 꺼낸 가격 **이후 시점**이다.
3. 앞에서부터 보면서 1초씩 센다. 가격이 떨어지면 그 1초까지 세고 `break`.
4. 탑 문제와 **방향만 반대**: 탑은 뒤에서 꺼내 왼쪽을 보고, 주식은 앞에서 꺼내 오른쪽을 본다.

### `[1, 2, 3, 2, 3]` 추적

| 꺼낸 가격 | 남은 가격 | 탐색 | 기간 |
|---|---|---|---|
| `1` | `[2, 3, 2, 3]` | 한 번도 안 떨어짐 | `4` |
| `2` | `[3, 2, 3]` | 한 번도 안 떨어짐 (`2`는 같으니 OK) | `3` |
| `3` | `[2, 3]` | `2`에서 바로 떨어짐 | `1` |
| `2` | `[3]` | 안 떨어짐 | `1` |
| `3` | `[]` | 볼 게 없음 | `0` |

→ `[4, 3, 1, 1, 0]`

- 코드 주석에 적어둔 대로, 큐는 **앞에서 꺼내는 용도로만** 쓰였고 결국 이중 반복이라 for문 풀이와 똑같이 **O(N²)**.

## 5. 해시 테이블 (Hash Table)

```python
class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)   # key → 숫자 → 배열 인덱스
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]
```

### 어떻게 동작하나
1. `hash(key)`: 문자열 같은 key를 **큰 정수**로 바꾼다. 같은 key는 항상 같은 정수가 나온다.
2. `% len(self.items)`: 그 정수를 **배열 크기로 나눈 나머지** → `0 ~ 7` 사이 인덱스가 된다.
3. 그 인덱스 칸에 값을 넣고(`put`), 똑같이 계산해서 꺼낸다(`get`).
4. 배열 인덱스 접근은 O(1)이니까, **탐색 없이 한 번에** 찾아간다.

```
"test" --hash()--> 2894571320 --% 8--> 0 --> items[0] = 3
```
(실제 `hash()` 값은 실행할 때마다 달라질 수 있다. 한 번 실행하는 동안에는 항상 같다.)

### 배열 vs 링크드 리스트 vs 해시

| | 인덱스로 찾기 | 값으로 찾기 | 중간 삽입/삭제 |
|---|---|---|---|
| 배열 | O(1) | O(N) | O(N) |
| 링크드 리스트 | O(N) | O(N) | O(1) (위치를 알 때) |
| 해시 테이블 | - | **O(1) (key로)** | O(1) |

### 문제: 충돌 (Collision)
- 칸은 8개뿐인데 key는 무한히 많다 → **서로 다른 key가 같은 인덱스**로 갈 수 있다.
- 위의 `Dict`는 그 칸에 **값만** 덮어쓰기 때문에:
  - `put("fast", 1)`, `put("slow", 2)`가 같은 칸이면 `"fast"`의 값이 사라진다.
  - `get("fast")`를 해도 `2`가 나온다. 누구 값인지 구분할 방법이 없다.

## 6. 충돌 해결: 체이닝 (Chaining)

> 각 칸에 값 하나가 아니라 **링크드 리스트**를 두고, 거기에 **`(key, value)` 쌍**을 줄줄이 달아둔다.

```python
class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:          # key까지 같이 저장했으니 비교할 수 있다
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())   # 칸마다 빈 LinkedTuple

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)
```

### 어떻게 동작하나
1. 인덱스 계산은 똑같다.
2. `put`: 그 칸의 리스트 **뒤에 `(key, value)`를 추가**한다. 덮어쓰지 않는다.
3. `get`: 그 칸의 리스트를 훑으면서 **key가 일치하는 쌍**의 value를 돌려준다.

```
"fast", "slow" 가 둘 다 index 3 으로 간 경우

items[3] → ("fast", 1) → ("slow", 2)

get("slow") → items[3]을 훑다가 key == "slow" 인 쌍 발견 → 2
```

- 충돌이 없으면 O(1), 한 칸에 몰리면 그 칸 리스트를 훑어야 해서 **최악 O(N)**.
- 실제로는 해시 함수가 골고루 흩뿌리고, 차면 배열 크기를 늘려서 **평균 O(1)** 을 유지한다.

### 다른 방법: 개방 주소법 (Open Addressing)
- 리스트를 달지 않고, **충돌하면 다음 빈 칸**을 찾아 넣는다. (`index + 1`, `index + 2`, ...)
- 파이썬 `dict`는 이 방식을 쓴다.

---

## 정리 한 줄

- **스택** = 한쪽 끝(`head`)만 쓴다 → LIFO. 파이썬은 `list`.
- **큐** = 양쪽 끝(`head`, `tail`)을 쓴다 → FIFO. 파이썬은 `deque`.
- **해시** = key를 인덱스로 바꿔 O(1)로 찾는다. 충돌은 **key까지 함께 저장**해서 해결 (체이닝).
- 탑 문제와 주식 문제는 "하나 꺼내고 나머지를 훑는" 같은 구조, 꺼내는 방향만 반대.
