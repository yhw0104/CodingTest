# Python 자료구조 정리: list vs array vs Linked List

## 1. 핵심 요약

| | Python list | array 모듈 | Linked List |
|---|---|---|---|
| 내부 구조 | 동적 배열 (포인터 배열) | 정적 타입 배열 (값 직접 저장) | 노드 + 포인터 체인 |
| 인덱스 조회 | O(1) | O(1) | O(N) |
| 끝에 추가 | O(1)* | O(1)* | O(1) (tail 포인터 있을 때) |
| 앞/중간 삽입 | O(N) | O(N) | O(1) (위치 알 때) |
| 앞/중간 삭제 | O(N) | O(N) | O(1) (위치 알 때) |
| 값 검색 | O(N) | O(N) | O(N) |
| 타입 혼용 | 가능 | 불가능 (단일 타입) | 가능 |
| 메모리 효율 | 낮음 | 높음 | 낮음 (포인터 추가) |

> \* amortized O(1) — 가끔 배열 재할당 발생

array / list
- 요소들에 접근하기 쉽다.
- 삽입과 삭제에 시간이 걸린다.

linked list
- 요소에 접근하려면 전체 linked list를 순회해야 한다.
- 삽입과 삭제가 더 빠르다.

---

## 2. 메모리 구조 비교

### Python list — 포인터 배열

```
list = [1, 2, 3]

메모리:
┌──────────┬──────────┬──────────┐
│ ptr→int  │ ptr→int  │ ptr→int  │  ← 연속된 포인터 배열 (8B씩)
└──────────┴──────────┴──────────┘
     ↓           ↓           ↓
  int(1)      int(2)      int(3)    ← 실제 객체 (각 28B, 메모리 곳곳에 분산)
```

- 정수 하나당 포인터(8B) + 파이썬 int 객체(28B) = **약 36B**
- 타입 혼용 가능한 이유: 포인터가 어떤 객체든 가리킬 수 있기 때문

### array 모듈 — 값 직접 저장

```python
import array
a = array.array('i', [1, 2, 3])

메모리:
┌────┬────┬────┐
│  1 │  2 │  3 │  ← 값 자체가 연속 메모리에 저장 (int: 4B씩)
└────┴────┴────┘
```

- 정수 하나당 **4B** (C 타입 기준)
- list 대비 메모리 약 **2~8배 절약**

### Linked List — 분산된 노드

```
[10|next] → [20|next] → [30|next] → [40|NULL]
 주소:0x1A    주소:0x7F    주소:0x3C    주소:0xB2
```

- 각 노드 = 데이터 + 다음 노드 주소(포인터)
- 메모리상 연속되지 않음 → 인덱스 계산 불가 → 조회가 O(N)인 이유

---

## 3. 자료구조별 상세 특징

### Python list

```python
a = [1, "hello", 3.14, True]  # 타입 혼용 가능

a[2]          # O(1) — 인덱스 조회
a.append(5)   # O(1) — 끝에 추가
a.pop()       # O(1) — 끝에서 제거
a.insert(0, 9) # O(N) — 앞에 삽입 (전체 이동)
a.pop(0)      # O(N) — 앞에서 제거 (전체 이동) ← 함정!
```

**장점**
- 범용성 최고 — 타입 혼용, 풍부한 메서드
- 파이썬에서 가장 기본적인 자료구조

**단점**
- 포인터 오버헤드로 메모리 소모 큼
- 앞/중간 삽입·삭제가 O(N)

### array 모듈

```python
import array
a = array.array('i', [1, 2, 3])  # 'i' = signed int
a = array.array('f', [1.1, 2.2]) # 'f' = float
a = array.array('d', [1.1, 2.2]) # 'd' = double

# 주요 타입 코드
# 'b' = signed char (1B)
# 'i' = signed int  (4B)
# 'f' = float       (4B)
# 'd' = double      (8B)
```

**장점**
- 메모리 효율 높음 (수백만 개 숫자 저장 시 유리)
- 바이너리 파일 I/O에 적합

**단점**
- 단일 타입만 저장 가능
- list보다 메서드 빈약

### Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드의 주소

class LinkedList:
    def __init__(self):
        self.head = None

    def append_front(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
```

**장점**
- 앞/중간 삽입·삭제 O(1) (위치를 이미 알 때)
- 크기가 동적으로 변하는 데이터에 유리

**단점**
- 인덱스 조회 O(N)
- 포인터 저장으로 메모리 오버헤드 추가
- 캐시 지역성(cache locality) 나쁨

---

## 4. 링크드리스트 조회가 O(N)인 이유

**"인덱스를 알면 O(1)이 되는 것 아닌가?"** → 불가능

list/array는 수학으로 주소를 즉시 계산할 수 있습니다.

```
a[3]의 주소 = 시작 주소 + (3 × 포인터 크기)  → O(1)
```

링크드리스트는 노드들이 메모리상 흩어져 있어 공식이 없습니다.

```
[10|0x7F] → [20|0x3C] → [30|0xB2] → [40|NULL]
  HEAD부터 포인터를 3번 따라가야만 [3]번 노드에 도달 가능 → O(N)
```

**"인덱스 3을 안다"는 것**은 숫자 3을 아는 것이지, 메모리 주소 0xB2를 아는 것이 아닙니다.

단, 노드 레퍼런스(객체 자체)를 직접 들고 있으면 O(1) 접근 가능합니다.

```python
node = linked_list.head.next.next  # 노드 객체를 변수로 보관
node.data  # O(1) — 인덱스가 아닌 레퍼런스로 접근
```

LRU 캐시가 이 방식을 활용합니다. `dict`에 `{키: 노드 레퍼런스}`를 저장해 O(1) 조회 + O(1) 이동/삭제를 구현합니다.

---

## 5. 알고리즘별 자료구조 선택 가이드

### 이진 탐색 (Binary Search)

```python
import bisect
a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)  # O(log N)
```

**→ list / array 사용**
중간 인덱스에 O(1) 접근이 핵심. Linked List는 중간까지 O(N) 순회가 필요해 이진 탐색 자체가 불가능.

---

### 스택 (Stack — LIFO)

```python
stack = []
stack.append(1)  # push O(1)
stack.pop()      # pop  O(1)
```

**→ list 사용**
끝에서만 push/pop하므로 list의 `append()`, `pop()`이 모두 O(1).

---

### 큐 (Queue — FIFO)

```python
from collections import deque

q = deque()
q.append(1)    # O(1)
q.popleft()    # O(1) ← list의 pop(0)은 O(N)!
```

**→ collections.deque 사용** (내부적으로 doubly linked list)

list의 `pop(0)`은 O(N)이므로 큐 패턴이 보이면 즉시 deque로 교체.

---

### 양방향 큐 (Deque)

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)  # O(1)
d.append(4)      # O(1)
d.popleft()      # O(1)
d.pop()          # O(1)
```

**→ collections.deque 사용**

---

### 잦은 중간 삽입/삭제

```python
# 위치(노드 레퍼런스)를 이미 알 때
node.next = new_node
new_node.next = node.next  # O(1) — 포인터 변경만
```

**→ Linked List 사용**

list는 삽입 지점 뒤 원소를 전부 밀어야 해서 O(N).

---

### LRU 캐시

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)
```

**→ Linked List + dict 조합** (또는 `functools.lru_cache`)

dict로 O(1) 조회, doubly linked list로 O(1) 이동/삭제.

---

### 수치 연산 / 대용량 숫자

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
a * 2        # [2, 4, 6, 8, 10] — 루프 없이 벡터 연산
a.mean()
a.sum()
```

**→ numpy array 사용** (array 모듈의 메모리 효율 + 벡터 연산)

---

### 정렬 알고리즘

```python
a = [3, 1, 4, 1, 5]
a.sort()     # O(N log N) — Timsort
sorted(a)    # O(N log N)
```

**→ list / array 사용**

파이썬 내장 정렬은 배열 기반 Timsort. Linked List는 랜덤 접근 불가로 정렬이 매우 비효율적.

---

## 6. list vs array 선택 기준

| 상황 | 선택 |
|---|---|
| 타입이 섞인 데이터 | `list` |
| 일반 알고리즘, 로직 구현 | `list` |
| 수백만 개 숫자 + 메모리 효율 중요 | `array` 또는 `numpy` |
| 수치 연산, 행렬, 통계 | `numpy` |
| 바이너리 파일 I/O 버퍼 | `array` |
| numpy 없는 환경에서 수치 데이터 | `array` |
| 그 외 모든 것 | `list` |

실무 의사결정 흐름:

```
숫자 데이터를 대량으로 다뤄야 하나?
├── YES → 수치 연산도 필요? → YES → numpy
│                           → NO  → array 모듈
└── NO  → list
```

---

## 7. 빠른 참조 — O(1) vs O(N) 체크리스트

**O(1)인 것들**
- `list[i]`, `array[i]` — 인덱스 조회
- `list.append()`, `list.pop()` — 끝 추가/제거
- `deque.appendleft()`, `deque.popleft()` — 앞 추가/제거
- Linked List HEAD/TAIL 접근
- Linked List 노드 레퍼런스를 직접 보유할 때 삽입/삭제

**O(N)인 것들 (함정 주의)**
- `list.pop(0)` — 앞에서 제거 ← 자주 실수하는 부분
- `list.insert(0, x)` — 앞에 삽입
- `x in list` — 값으로 검색
- `list.index(x)` — 값으로 인덱스 찾기
- Linked List 인덱스 조회 (HEAD부터 순회)