# 자료구조 초기화 · 세팅 정리

1~4주차에 작성한 코드에서 **리스트, 링크드 리스트, 스택, 큐, 해시(딕셔너리), 힙, 그래프**를 어떻게 만들고 세팅했는지 모아 둔 문서.
각 자료구조마다 **① 직접 구현(클래스)** 과 **② 코테에서 바로 쓰는 파이썬 내장 방식**을 같이 정리했다.

| 자료구조 | 직접 구현 초기화 | 코테용 초기화 | 참고 파일 |
|---|---|---|---|
| 리스트 | - | `arr = []`, `[0] * n` | `03_07`, `03_09`, `03_12` |
| 링크드 리스트 | `self.head = Node(value)` | (거의 안 씀) | `2_2`, `2_3`, `2_4`, `2_11` |
| 스택 | `self.head = None` | `stack = []` | `03_06`, `04_04` |
| 큐 | `self.head = None`, `self.tail = None` | `queue = deque()` | `03_08`, `03_09`, `04_05` |
| 해시 | `self.items = [None] * 8` | `dic = {}` | `03_10`, `03_11`, `03_14` |
| 힙 | `self.items = [None]` | `heap = []` + `heapq` | `04_01`, `04_02` |
| 그래프 | - | `graph = {1: [2, 5], ...}` | `04_03`, `04_04`, `04_05` |

---

## 1. 리스트 (List / Array)

### 초기화

```python
arr = []                          # 빈 리스트
arr = [1, 2, 3, 4, 5]             # 값을 넣어서
answer = [0] * len(heights)       # 길이 n, 0으로 채우기 (03_07, 03_09)
items = [None] * 8                # 길이 8, None으로 채우기 (03_10)
array = list(string)              # 문자열 → 문자 리스트 (03_13)  "(())" → ['(', '(', ')', ')']
```

> 2차원 리스트는 `[[0] * m for _ in range(n)]` 로 만든다.
> `[[0] * m] * n` 은 **같은 리스트를 n번 참조**해서 한 칸만 바꿔도 모든 행이 같이 바뀐다.

### 자주 쓴 세팅 / 조작

```python
arr.append(x)                     # 맨 뒤에 추가          O(1)
arr.pop()                         # 맨 뒤 꺼내기          O(1)
arr.pop(i)                        # i번째 꺼내기          O(N)
arr.index(x)                      # x의 첫 위치           O(N)
len(arr)

arr.sort()                        # 오름차순 (제자리 정렬, 반환값 None)  (2_12)
arr.sort(reverse=True)            # 내림차순                          (03_12)
sorted_arr = sorted(arr, key=lambda item: item[1], reverse=True)  # 새 리스트 반환 (03_14)

for i in range(len(arr) - 1, -1, -1):   # 뒤에서부터 순회 (03_07)
    ...
```

---

## 2. 링크드 리스트 (Linked List)

### 초기화: `Node` + `LinkedList`

```python
class Node:
    def __init__(self, data):
        self.data = data      # 값
        self.next = None      # 다음 노드 (처음엔 없음)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)   # 첫 노드를 만들어 head로 둔다
```

- 내가 짠 링크드 리스트는 **생성할 때 첫 값을 받아서 head를 바로 만든다.**
- 그래서 빈 링크드 리스트는 만들 수 없다. (스택/큐는 `head = None`으로 시작하는 것과 차이)

### 세팅 (값 채우기)

```python
def append(self, value):
    cur = self.head
    while cur.next is not None:   # 마지막 노드까지 이동
        cur = cur.next
    cur.next = Node(value)        # 마지막 노드 뒤에 붙이기  → O(N)

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)             # [6] -> [7] -> [8]
```

### 순회 기본형

```python
cur = self.head
while cur is not None:            # 모든 노드 방문
    print(cur.data)
    cur = cur.next
```

| 하고 싶은 것 | 조건 | 쓰는 곳 |
|---|---|---|
| 모든 노드 방문 | `while cur is not None` | `print_all`, 길이 세기 |
| 마지막 노드에서 멈추기 | `while cur.next is not None` | `append` |
| index 번째 노드로 가기 | `for _ in range(index): cur = cur.next` | `find_by_index` |

### 중간 삽입 / 삭제 (2_3)

```python
# index 자리에 삽입: 앞 노드를 찾고 → 새 노드가 뒤를 잡고 → 앞 노드가 새 노드를 잡는다
add.next = cur.next
cur.next = add

# index 자리 삭제: 앞 노드가 다음다음 노드를 가리키게
prev_node.next = prev_node.next.next

# index == 0 이면 head 자체를 바꿔야 한다
self.head = new_node         # 삽입
self.head = self.head.next   # 삭제
```

---

## 3. 스택 (Stack) — LIFO

### ① 직접 구현 (03_06)

```python
class Stack:
    def __init__(self):
        self.head = None          # 빈 스택으로 시작

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head # 새 노드가 기존 top을 가리키고
        self.head = new_head      # top 교체

    def pop(self):
        if self.is_empty():
            return "stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
```

### ② 코테용: 그냥 리스트 (04_04)

```python
stack = []                # 빈 스택
stack = [start_node]      # 시작값을 넣고 시작 (DFS)

stack.append(x)           # push
stack.pop()               # pop
stack[-1]                 # peek
while stack:              # 비어있지 않은 동안 반복 (빈 리스트는 False)
    ...
```

---

## 4. 큐 (Queue) — FIFO

### ① 직접 구현 (03_08)

```python
class Queue:
    def __init__(self):
        self.head = None          # 꺼내는 쪽
        self.tail = None          # 넣는 쪽

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return                # ← 비어 있을 땐 여기서 끝내야 한다
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None
```

> ⚠️ `03_08_queue.py` 원본에는 비어 있을 때 `return`이 없어서, 첫 노드가 `self.tail.next = new_node`로 **자기 자신을 가리키게** 된다.
> 빈 큐에 1개만 넣고 `dequeue()`하면 `head = head.next`가 다시 자기 자신이라 큐가 영영 비지 않는다.
> (뒤에 다른 값을 더 넣으면 `next`가 덮어써져서 지금 테스트 코드에선 드러나지 않음) 위처럼 `return`을 넣으면 해결된다.

### ② 코테용: `deque` (03_09)

```python
from collections import deque

queue = deque()               # 빈 큐
queue = deque([start_node])   # 시작값 넣고 시작 (BFS)
prices = deque(prices)        # 기존 리스트 → 큐

queue.append(x)               # enqueue      O(1)
queue.popleft()               # dequeue      O(1)
queue[0]                      # peek
while queue:
    ...
```

> `04_05_bfs_queue.py`는 `queue = [start_node]` + `queue.pop(0)`을 썼다. 동작은 같지만 `list.pop(0)`은 **O(N)** 이라
> 데이터가 많으면 `deque.popleft()`(O(1))로 바꾸는 게 좋다.

---

## 5. 해시 테이블 (Dictionary)

### ① 직접 구현 (03_10)

```python
class Dict:
    def __init__(self):
        self.items = [None] * 8                   # 칸 8개짜리 배열

    def put(self, key, value):
        index = hash(key) % len(self.items)       # key → 인덱스
        self.items[index] = value
```

충돌 해결(체이닝, `03_10_dict_chaining.py`)은 **각 칸에 리스트를 하나씩** 넣어서 초기화한다.

```python
class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())      # 칸마다 (key, value) 목록

class LinkedTuple:
    def __init__(self):
        self.items = []                           # [(key, value), ...]
```

### ② 코테용: `dict`

```python
dic = {}                                  # 빈 딕셔너리
memo = {1: 1, 2: 1}                       # 초기값 넣어서 (04_07)

for student in all_array:                 # 리스트 → dict 세팅 (03_11)
    dic[student] = True

del dic[key]                              # 삭제
key in dic                                # 존재 확인  O(1)
dic.keys() / dic.values() / dic.items()
```

**키가 없으면 새로 만들고, 있으면 누적하는 패턴 (03_14)**

```python
if genre in total_dict:
    total_dict[genre] += play
    index_dict[genre].append([i, play])
else:
    total_dict[genre] = play              # 숫자로 시작
    index_dict[genre] = [[i, play]]       # 리스트로 시작

# dict 를 값 기준으로 정렬
sorted(total_dict.items(), key=lambda item: item[1], reverse=True)
```

---

## 6. 힙 (Heap)

### ① 직접 구현 (04_01, 04_02)

```python
class MaxHeap:
    def __init__(self):
        self.items = [None]       # 0번 칸은 비워두고 1번부터 사용
```

- 0번을 비워두면 인덱스 계산이 깔끔해진다.
  - 부모: `index // 2`
  - 왼쪽 자식: `index * 2`
  - 오른쪽 자식: `index * 2 + 1`
- 루트(최댓값)는 항상 `self.items[1]`.

### ② 코테용: `heapq` (최소 힙)

```python
import heapq

heap = []                       # 빈 힙
heapq.heappush(heap, x)         # 삽입  O(logN)
heapq.heappop(heap)             # 최솟값 꺼내기  O(logN)
heap[0]                         # 최솟값 보기
heapq.heapify(arr)              # 기존 리스트를 힙으로  O(N)

heapq.heappush(heap, -x)        # 최대 힙이 필요하면 음수로 넣고
-heapq.heappop(heap)            # 꺼낼 때 다시 음수
```

---

## 7. 그래프 (인접 리스트)

### 초기화 (04_03 ~ 04_05)

```python
graph = {
    1: [2, 5, 9],     # 1번 노드와 연결된 노드들
    2: [1, 3],
    3: [2, 4],
    ...
}
visited = []          # 방문 기록
```

간선 목록으로 주어질 때는 직접 세팅한다.

```python
graph = {i: [] for i in range(1, n + 1)}
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)    # 양방향이면 둘 다
```

> `visited`를 리스트로 두면 `x not in visited`가 O(N)이다. `visited = set()` 또는 `visited = [False] * (n + 1)`로 두면 O(1).

### DFS / BFS 시작 세팅 비교

| | 자료구조 | 시작 세팅 | 꺼내기 |
|---|---|---|---|
| DFS (재귀) | 호출 스택 | `dfs(graph, 1, visited)` | - |
| DFS (반복) | 스택 | `stack = [start_node]` | `stack.pop()` |
| BFS | 큐 | `queue = deque([start_node])` | `queue.popleft()` |

---

## 8. 메모이제이션 (04_07)

```python
memo = {
    1: 1,
    2: 1,             # 이미 아는 답(base case)을 미리 넣어두고 시작
}

if n in memo:         # 계산한 적 있으면 바로 반환
    return memo[n]
```
