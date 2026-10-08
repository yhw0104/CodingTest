# 4주차 트리와 힙, BFS와 DFS 그리고 DP 정리

> 출처: `4주차_트리와_힙_BFS와_DFS_그리고_DP.pdf` (이론 마지막 주차)

**수업 목표**
- 트리, 힙의 개념과 활용법
- 그래프, BFS, DFS
- Dynamic Programming의 개념과 필요성

| 주제 | 한 줄 요약 | 핵심 연산 / 복잡도 | 내 코드 |
|---|---|---|---|
| 트리 | 계층 구조를 표현하는 **비선형** 자료구조 | 완전 이진 트리 높이 O(logN) | - |
| 힙 | 최댓값/최솟값을 빠르게 뽑기 위한 **완전 이진 트리** | 삽입·삭제 O(logN) | `04_01`, `04_02` |
| 그래프 | 노드 사이의 **연결 관계**를 표현 | 인접 행렬 / 인접 리스트 | - |
| DFS | **끝까지 파고든** 뒤 되돌아오는 탐색 | 재귀 또는 **스택** | `04_03`, `04_04` |
| BFS | **가까운 것부터** 넓게 퍼지는 탐색 | **큐** | `04_05` |
| DP | 부분 문제의 답을 **기록해두고 재사용** | 메모이제이션 | `04_06`, `04_07` |
| 숙제 | 라면 공장 / 로봇 청소기 / 극장 좌석 | 힙 / BFS / DP | `04_08` |

---

## 1. 트리 (Tree)

### 1-1. 트리란?

> 뿌리와 가지로 구성되어 거꾸로 세워놓은 나무처럼 보이는 **계층형 비선형 자료구조**

| | 선형 구조 | 비선형 구조 |
|---|---|---|
| 예시 | 큐, 스택, 링크드 리스트 | **트리**, 그래프 |
| 모양 | 데이터가 순차적으로 나열됨 | 계층적 혹은 망으로 구성됨 |
| 초점 | 자료를 **저장하고 꺼내는 것** | 자료를 **표현하는 것** |

대표적인 트리 형태: 컴퓨터의 **폴더 구조**

### 1-2. 용어

```
            A          Level 0   ← Root Node
          /   \
         B     C       Level 1
        / \     \
       D   E     F     Level 2   ← D, E, F는 Leaf Node
```

| 용어 | 뜻 |
|---|---|
| Node | 트리에서 데이터를 저장하는 기본 요소 |
| Root Node | 트리 맨 위에 있는 노드 |
| Level | 최상위 노드를 Level 0으로 했을 때, 하위 Branch로 연결된 노드의 깊이 |
| Parent Node | 어떤 노드의 상위 레벨에 연결된 노드 |
| Child Node | 어떤 노드의 하위 레벨에 연결된 노드 |
| Leaf Node (Terminal Node) | Child Node가 하나도 없는 노드 |
| Sibling | 동일한 Parent Node를 가진 노드 |
| Depth | 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수 |

### 1-3. 트리의 종류

이진 트리, 이진 탐색 트리, 균형 트리(AVL, red-black), 이진 힙(최대힙, 최소힙) 등 다양하지만
수업에서는 **이진 트리**와 **완전 이진 트리**만 다룬다.

**이진 트리 (Binary Tree)**: 각 노드가 **최대 두 개**의 자식을 가진다. (0, 1, 2개만 가능)

```
      o      Level 0
    o o o    Level 1      ← 자식이 3개 → 이진 트리 ❌
   o  o  o   Level 2

      o      Level 0
    o   o    Level 1
   o o o     Level 2      ← 이진 트리 ⭕
```

**완전 이진 트리 (Complete Binary Tree)**: 노드를 삽입할 때 **최하단 왼쪽 노드부터 차례대로** 삽입해야 한다.

```
      o      Level 0
    o   o    Level 1
     o o     Level 2      ← 왼쪽 자리가 비어 있음 → 이진 트리 ⭕ / 완전 이진 트리 ❌

      o      Level 0
    o   o    Level 1
   o o o     Level 2      ← 왼쪽부터 빈틈없이 → 이진 트리 ⭕ / 완전 이진 트리 ⭕
```

### 1-4. 완전 이진 트리를 배열로 표현

트리는 **클래스로 직접 구현**하거나 **배열로 표현**할 수 있다.
완전 이진 트리는 왼쪽부터 데이터가 쌓이므로, **순서대로 배열에 쌓으면** 표현할 수 있다.

편의를 위해 **0번째 인덱스는 사용하지 않고** `None`을 넣고 시작한다.

```
      8      Level 0   → [None, 8]
    6   3    Level 1   → [None, 8, 6, 3]
   4 2 5     Level 2   → [None, 8, 6, 3, 4, 2, 5]

index:   0    1  2  3  4  5  6
       [None, 8, 6, 3, 4, 2, 5]
```

| 찾고 싶은 것 | 계산식 | 예시 (index 1의 8 기준) |
|---|---|---|
| 왼쪽 자식 | `현재 인덱스 * 2` | 1 * 2 = 2 → **6** |
| 오른쪽 자식 | `현재 인덱스 * 2 + 1` | 1 * 2 + 1 = 3 → **3** |
| 부모 | `현재 인덱스 // 2` | 3의 부모: 3 // 2 = 1 → **8** |

### 1-5. 완전 이진 트리의 높이

**높이(Height)** = 루트 노드부터 가장 아래 리프 노드까지의 길이

```
      1            Level 0   1개
    2   3          Level 1   2개
   4 5 6 7         Level 2   4개
 8 9 ...  14 15    Level 3   8개
                   Level k   2^k 개
```

- 레벨 k에 최대로 들어갈 수 있는 노드 수: **2^k**
- 높이가 h이고 꽉 찬 트리의 전체 노드 수: `1 + 2 + 4 + ... + 2^h` = **2^(h+1) - 1**
- 노드 수가 N이면 `2^(h+1) - 1 = N` → **h = log₂(N+1) - 1**
- 즉, 완전 이진 트리의 높이는 최대 **O(logN)**

> 예: h = 8 → N = 2^9 - 1 = 511 / 반대로 N = 511 → h = log₂512 - 1 = 8

---

## 2. 힙 (Heap)

### 2-1. 힙이란?

> 데이터에서 **최댓값과 최솟값을 빠르게 찾기 위해** 고안된 **완전 이진 트리**

**🏥 응급실 비유**
- 감기, 골절, 출혈 환자가 오면 우선순위대로 **출혈 → 골절 → 감기** 순으로 치료한다.
  → 힙은 특정 순서에 맞춰 **항상 데이터를 정렬된 상태로 유지**한다. 꺼낼 때 항상 순서대로 가져온다.
- 심정지 환자가 새로 오면 가장 높은 우선순위를 줘서 맨 앞으로 보낸다.
  → 새 데이터가 추가되면 **다시 순서에 맞게 정렬**해준다.

**Q. 정렬이랑 뭐가 다른가요?**

| | 정렬 | 힙 |
|---|---|---|
| 비용 | 매번 **O(NlogN)** | 넣고 빼는 데 **O(logN)** |
| 특징 | 데이터가 바뀌면 다시 정렬 | 매번 정렬하지 않아도 정렬된 상태 유지 |

→ **삽입·삭제가 잦은데 항상 최대/최소가 필요한 상황**이면 힙이 더 효율적이다.

### 2-2. 힙의 규칙

- 부모 노드의 값이 **항상** 자식 노드의 값보다 커야 한다. → 가장 큰 값이 맨 위(루트)로 간다.
- 최댓값이 맨 위면 **Max 힙**, 최솟값이 맨 위면 **Min 힙**.

```
      8
    6   3          ← 완전 이진 트리 ❌ → 힙 아님
     2 1

      8
    6   3          ← 완전 이진 트리 ⭕ + 부모가 항상 큼 → 힙 ⭕
   4 2 1

      8
    6   3          ← 3의 자식 5가 더 큼 → 힙 아님
   4 2 5
```

> 형제끼리는 크기 순서가 정해져 있지 않다. 부모 ↔ 자식 관계만 지키면 된다.

> ⚠️ **"최댓값과 최솟값을 빠르게 찾는다"는 둘 다 동시에가 아니라, 힙 종류에 따라 하나만이다.**
> - Max 힙 → 최댓값만 O(1) (`items[1]`) / Min 힙 → 최솟값만 O(1)
> - Max 힙에서 **최솟값은 맨 끝이 아니다.** 리프 노드 중 어딘가에 있을 뿐이다.
>
> ```
>       8
>     6   3        items = [None, 8, 6, 3, 4, 1, 2]
>    4 1 2         맨 끝은 2지만 최솟값은 1
> ```
>
> - Max 힙에서 최솟값을 찾으려면 리프들(대략 절반)을 다 봐야 해서 O(N).
> - 둘 다 빨리 필요하면 Max 힙과 Min 힙을 **두 개** 같이 쓴다.

### 2-3. 맥스 힙에 원소 추가 (`04_01`)

**방법**
1. 원소를 **맨 마지막**에 넣는다.
2. 부모 노드와 비교해서 더 크다면 자리를 바꾼다.
3. 부모보다 작거나 **가장 위에 도달할 때까지** 2를 반복한다.

**예시: 9 추가**

```
      8               8               8               9
    6   3     →     6   3     →     6   9     →     6   8
   4 2 1           4 2 1 9         4 2 1 3         4 2 1 3
               ① 맨 끝에 추가   ② 9 > 3 교체     ③ 9 > 8 교체, 꼭대기 도착
```

```python
class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1     # 방금 넣은 맨 끝 인덱스부터 시작

        while cur_index > 1:                # 1이 되면 꼭대기라 비교할 필요 없음
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3]
```

**시간 복잡도**: 맨 밑에서 꼭대기까지 비교하며 올라간다 → 최대 높이만큼 반복 → **O(logN)**

### 2-4. 맥스 힙의 원소 제거 (`04_02`)

힙에서 삭제는 **항상 루트(최댓값)만** 제거한다. (스택처럼 맨 위만 뺄 수 있다)

**방법**
1. 루트 노드와 **맨 끝 원소를 교체**한다.
2. 맨 뒤 원소(원래 루트)를 삭제한다. → 이게 최댓값이므로 **마지막에 반환**
3. 바뀐 노드를 자식들과 비교한다. **두 자식 중 더 큰 자식**이 자신보다 크면 자리를 바꾼다.
4. 자식 둘보다 크거나 **가장 바닥에 도달할 때까지** 3을 반복한다.
5. 2에서 제거한 원래 루트를 반환한다.

**예시**

```
      8                3                3                7                7
    6   7      →     6   7      →     6   7      →     6   3      →     6   4
   2 5 4 3          2 5 4 8          2 5 4            2 5 4            2 5 3
               ① 8 ↔ 3 교체     ② 8 제거          ③ 6,7 중 7이 크고  ④ 4 > 3 교체
                                                    3보다 큼 → 교체     바닥 도착 → 8 반환
```

```python
def delete(self):
    self.items[1], self.items[-1] = self.items[-1], self.items[1]   # 1. 루트 ↔ 맨 끝
    prev_max = self.items.pop()                                      # 2. 원래 루트 꺼내기
    cur_index = 1

    while cur_index <= len(self.items) - 1:
        left_child_index = cur_index * 2
        right_child_index = cur_index * 2 + 1
        max_index = cur_index

        # 자식 인덱스가 배열 크기를 넘지 않는지 꼭 확인
        if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
            max_index = left_child_index
        if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
            max_index = right_child_index

        if max_index == cur_index:          # 부모가 두 자식보다 크다 → 멈춤
            break

        self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
        cur_index = max_index

    return prev_max                          # 5. 원래 루트 반환

# insert 8, 6, 7, 2, 5, 4 후
# items    → [None, 8, 6, 7, 2, 5, 4]
# delete() → 8
# items    → [None, 7, 6, 4, 2, 5]
```

**시간 복잡도**: 맨 위에서 바닥까지 비교하며 내려간다 → **O(logN)**

### 2-5. 파이썬 `heapq` 모듈

직접 구현하지 않아도 `heapq`가 힙 구조를 유지하며 넣고 빼준다. 기본은 **최소 힙**.

```python
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)                  # [1, 3, 7, 4]   heap[0]이 최솟값
print(heapq.heappop(heap))   # 1             최솟값 꺼내기
print(heap)                  # [3, 4, 7]
```

> PDF에는 `[3, 7, 4]`로 적혀 있지만 실제로 실행하면 `[3, 4, 7]`이 나온다. 맨 끝의 4가 루트로 올라간 뒤 더 작은 자식 3과 자리를 바꾸기 때문이다.

**최대 힙이 필요하면 -1을 곱해서** 넣고, 꺼낼 때도 -1을 곱한다.

```python
heap = []
heapq.heappush(heap, 4 * -1)
heapq.heappush(heap, 1 * -1)
heapq.heappush(heap, 7 * -1)
heapq.heappush(heap, 3 * -1)
print(heap)                       # [-7, -3, -4, -1]
print(heapq.heappop(heap) * -1)   # 7   최댓값 꺼내기
print(heap)                       # [-4, -3, -1]
```

---

## 3. 그래프 (Graph)

### 3-1. 그래프란?

> 연결되어 있는 정점과 정점 간의 **관계**를 표현할 수 있는 자료구조

- 선형 구조: 저장·꺼내기에 초점 / 비선형 구조: 표현에 초점
- 그래프는 그중에서도 **연결 관계**에 초점이 맞춰져 있다.
- 예: 페이스북 친구 관계. 나 - 로제 - 사나 → 사나와 나는 2촌

| 용어 | 뜻 |
|---|---|
| 노드 (Node) | 연결 관계를 가진 각 데이터. **정점(Vertex)** 이라고도 함 |
| 간선 (Edge) | 노드 간의 관계를 표시한 선 |
| 인접 노드 (Adjacent Node) | 간선으로 **직접** 연결된 노드 |

```
          로제 - 사나
           |
    제니 - 딩코

딩코: 노드 / 딩코-제니: 간선으로 연결 / 딩코와 로제: 인접 노드
```

| 종류 | 특징 |
|---|---|
| 유방향 그래프 (Directed) | 방향이 있는 간선. 한 방향으로만 진행 가능 |
| 무방향 그래프 (Undirected) | 방향이 없는 간선. **수업에서는 무방향만 다룸** |

### 3-2. 그래프의 표현 방법

번호를 붙여서 표현: 제니 0, 딩코 1, 로제 2, 사나 3

```
      2 - 3
      |
  0 - 1
```

**① 인접 행렬 (Adjacency Matrix)**: 2차원 배열로 연결 관계 표현

```python
#      0      1      2      3
graph = [
    [False, True,  False, False],   # 0
    [True,  False, True,  False],   # 1
    [False, True,  False, True ],   # 2
    [False, False, True,  False],   # 3
]
graph[1][2]   # 연결 여부 바로 확인 → O(1)
```

**② 인접 리스트 (Adjacency List)**: 각 노드에 연결된 노드 목록을 저장

```python
graph = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2],
}
# 연결 여부를 보려면 graph[0]의 원소를 다 봐야 함
```

**차이: 시간 vs 공간**

| | 인접 행렬 | 인접 리스트 |
|---|---|---|
| 연결 여부 확인 | **O(1)** 즉시 | 최대 **O(간선)** |
| 공간 | **O(노드²)** 모든 조합 저장 | **O(노드 + 간선)** |

---

## 4. DFS & BFS

### 4-1. 왜 배울까?

- 이분 탐색처럼 효율적인 방법도 있지만, **모든 경우의 수를 전부 탐색**해야 하는 경우도 있다. (예: 알파고)
- DFS와 BFS는 **탐색 순서**가 다르다.

| | DFS (Depth First Search) | BFS (Breadth First Search) |
|---|---|---|
| 방식 | **끝까지 파고든다** | 갈라진 **모든 경우를 탐색**하고 온다 |
| 공간 | 그래프의 최대 깊이만큼 → **적게 씀** | 모든 분기를 저장 → **많이 씀** |
| 최단 경로 | 찾기 **쉽지 않음** | **쉽게 찾음** |
| 시간 | - | 모든 걸 다 보고 와서 더 걸릴 수 있음 |
| 구현 | 재귀 / **스택** | **큐** |

### 4-2. DFS - 재귀함수 (`04_03`)

갈 수 있는 만큼 계속 탐색하다가, 갈 수 없게 되면 다른 방향으로 다시 탐색한다.
→ "반복하다가 갈 수 없으면 탈출" = **재귀함수**

```
DFS(node) = node + DFS(node와 인접하지만 방문하지 않은 다른 node)
```

방문 여부는 `visited` 배열에 기록해서 확인한다.

1. 루트 노드부터 시작한다.
2. 현재 방문한 노드를 `visited`에 추가한다.
3. 현재 노드와 인접한 노드 중 방문하지 않은 노드에 방문한다.
4. 2부터 반복한다.

```python
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

dfs_recursion(graph, 1, visited)
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```
        1
     /  |  \
    2   5   9         방문 순서: 1 → 2 → 3 → 4 (막힘, 되돌아감)
    |  / \   \                  → 5 → 6 → 7 (막힘) → 8 (막힘)
    3 6   8   10                → 9 → 10 → 끝
    |  |
    4  7
```

### 4-3. DFS - 스택 (`04_04`)

**재귀의 문제**: 노드가 무한정 깊어지면 `RecursionError`가 날 수 있다.

DFS = 방문하지 않은 인접 노드를 모두 저장해두고, **가장 마지막에 넣은 노드**부터 꺼내 탐색
→ 가장 마지막에 넣은 것 = **스택**

1. 루트 노드를 스택에 넣는다.
2. 스택에서 노드를 빼서 `visited`에 추가한다.
3. 현재 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.
4. 2부터 반복한다.
5. 스택이 비면 종료한다.

```python
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

print(dfs_stack(graph, 1))  # [1, 9, 10, 5, 8, 6, 7, 2, 3, 4]
```

| 단계 | 꺼낸 노드 | stack (오른쪽이 top) | visited |
|---|---|---|---|
| 시작 | - | `[1]` | `[]` |
| 1 | 1 | `[2, 5, 9]` | `[1]` |
| 2 | 9 | `[2, 5, 10]` | `[1, 9]` |
| 3 | 10 | `[2, 5]` | `[1, 9, 10]` |
| 4 | 5 | `[2, 6, 8]` | `[1, 9, 10, 5]` |
| 5 | 8 | `[2, 6]` | `[..., 8]` |
| 6 | 6 | `[2, 7]` | `[..., 6]` |
| 7 | 7 | `[2]` | `[..., 7]` |
| 8 | 2 | `[3]` | `[..., 2]` |
| 9 | 3 | `[4]` | `[..., 3]` |
| 10 | 4 | `[]` | `[1, 9, 10, 5, 8, 6, 7, 2, 3, 4]` |

> 재귀 방식과 **탐색 순서는 다르지만** (스택은 마지막에 넣은 9부터 꺼냄) **가장 깊게 탐색하는 방식은 똑같다.**
> 구현의 차이일 뿐 개념은 동일하다.

### 4-4. BFS - 큐 (`04_05`)

BFS = 방문하지 않은 인접 노드를 모두 저장해두고, **가장 처음에 넣은 노드**부터 꺼내 탐색
→ 가장 처음에 넣은 것 = **큐**

1. 루트 노드를 큐에 넣는다.
2. 큐에서 노드를 빼서 `visited`에 추가한다.
3. 현재 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다.
4. 2부터 반복한다.
5. 큐가 비면 종료한다.

```python
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []
    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
    return visited

print(bfs_queue(graph, 1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

```
          1                Level 0: 1
       /  |  \
      2   3   4            Level 1: 2, 3, 4
      |  / \   \
      5 6   7   8          Level 2: 5, 6, 7, 8
      | |
      9 10                 Level 3: 9, 10
```

| 단계 | 꺼낸 노드 | queue (왼쪽이 front) | visited |
|---|---|---|---|
| 시작 | - | `[1]` | `[]` |
| 1 | 1 | `[2, 3, 4]` | `[1]` |
| 2 | 2 | `[3, 4, 5]` | `[1, 2]` |
| 3 | 3 | `[4, 5, 6, 7]` | `[1, 2, 3]` |
| 4 | 4 | `[5, 6, 7, 8]` | `[..., 4]` |
| 5 | 5 | `[6, 7, 8, 9]` | `[..., 5]` |
| 6 | 6 | `[7, 8, 9, 10]` | `[..., 6]` |
| 7~10 | 7, 8, 9, 10 | `[]` | `[1, 2, ..., 10]` |

> 💡 **DFS 스택 코드와 BFS 코드는 `stack.pop()` ↔ `queue.pop(0)` 한 줄만 다르다.**

#### 보충: 코드 개선 포인트 (PDF 외)
- `list.pop(0)`은 O(N) → `collections.deque`의 `popleft()`(O(1))를 쓰는 게 좋다.
- `visited`가 리스트면 `in` 검사가 O(N) → `set`을 쓰면 O(1).
- 이 코드는 **꺼낼 때** 방문 처리를 하므로, **사이클이 있는 그래프**에서는 같은 노드가 두 번 들어갈 수 있다.
  - 예: 삼각형 `{1: [2, 3], 2: [1, 3], 3: [1, 2]}` → DFS `[1, 3, 2, 2]`, BFS `[1, 2, 3, 3]`
  - 무방향이라 생기는 자식 → 부모 간선은 부모가 이미 `visited`라 괜찮다. 문제는 **두 경로로 같은 노드에 닿는 사이클**.
  - PDF의 Java/JS 답안은 `queued` 집합으로 **큐에 넣을 때** 체크해서 이를 막는다.

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}               # 넣을 때 방문 처리
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return order
```

---

## 5. Dynamic Programming (동적 계획법)

### 5-1. 피보나치 수열 - 재귀함수 (`04_06`)

> 첫째, 둘째 항이 1이고, 그 뒤 모든 항은 **바로 앞 두 항의 합**인 수열. 1, 1, 2, 3, 5, 8, ...

```
Fibo(1) = 1, Fibo(2) = 1
Fibo(n) = Fibo(n - 1) + Fibo(n - 2)
```

비슷한 구조의 반복 → **재귀함수**로 풀 수 있다. 탈출 조건은 n이 1 또는 2일 때 1 반환.

```python
input = 20

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

print(fibo_recursion(input))  # 6765
```

**단점: input을 100으로 바꾸면 값이 나오지 않는다.**

```
                 Fibo(5)
              /           \
         Fibo(4)          Fibo(3)      ← Fibo(3)을 또 계산
         /     \          /     \
    Fibo(3)  Fibo(2)  Fibo(2)  Fibo(1)
     /    \
Fibo(2)  Fibo(1)
```

- Fibo(3) 연산량 2번 → Fibo(4) 3번 → Fibo(5) 5번 → ... 점점 폭발적으로 늘어남
- **이미 했던 작업을 다른 곳에서 다시 새롭게 하고 있다.**
- 이런 "삽질"을 안 하려면 **이미 했던 일을 기록**해야 한다. → 동적 계획법

> 📝 내 코드 `04_06`은 `input = 100`으로 되어 있어서 끝나지 않는다. PDF 문제는 **20번째 수(6765)** 를 구하는 것.

### 5-2. 동적 계획법이란?

**🚇 출근길 비유**: 집 → 봉천역 → 삼성역 → 코엑스, 구간마다 지하철/버스/따릉이/킥보드 중 선택

- 모든 조합을 매일 다 실험해봐야 할까? → **각 구간마다** 얼마나 걸리는지만 알면 된다.
- 이미 실험한 시간은 다시 시도하지 않고 **기록해두면** 된다.

> 📖 **동적 계획법(Dynamic Programming)**: 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법.
> 부분 문제 반복과 최적 부분 구조를 가지고 있는 알고리즘을 더 적은 시간 내에 풀 때 사용한다.

- 여러 개의 하위 문제를 풀고, **그 결과를 기록하고 이용해** 문제를 해결하는 알고리즘
- 재귀처럼 문제를 쪼개서 수식으로 정의할 수 있으면 DP를 쓸 수 있다.
- 재귀와의 차이: **결과를 기록하고 이용한다**

| 용어 | 뜻 | 출근길 비유 |
|---|---|---|
| 메모이제이션 (Memoization) | 결과를 **기록**하는 것 | 이미 실험한 내용은 기록해두고 씀 |
| 겹치는 부분 문제 (Overlapping Subproblem) | 문제를 **쪼갤 수 있는** 구조 | 각 구간의 시간을 계산하면 최적 시간을 구할 수 있음 |

→ **겹치는 부분 문제일 경우 DP를 쓰고, 이때 메모이제이션을 이용한다.**

### 5-3. 피보나치 수열 - 동적 계획법 (`04_07`)

1. 메모용 데이터를 만든다. Fibo(1), Fibo(2)는 각각 1로 저장해둔다.
2. Fibo(n)을 구할 때 메모에 값이 있으면 **바로 반환**한다.
3. Fibo(n)을 처음 구했다면 메모에 **기록**한다.

```
fibo(5)를 찾아와라!
 1. memo[5] 있나? 없음 → fibo(4) + fibo(3) 필요
 2. memo[4] 있나? 없음 → fibo(3) + fibo(2) 필요
 3. memo[3] 있나? 없음 → fibo(2) + fibo(1) 필요
 4. memo[2], memo[1] 있음 → 더해서 fibo(3), memo[3]에 기록
 5. memo[3] + memo[2] → fibo(4), memo[4]에 기록
 6. memo[3] 있음! (4에서 기록해둠) → 바로 가져옴
 7. memo[4] + memo[3] → fibo(5), memo[5]에 기록
```

```python
input = 50

memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))  # 12586269025
```

- 재귀로는 100번째도 못 구했는데, 이번엔 **엄청나게 빠르게** 반환된다.
- DP는 성능 향상뿐 아니라 **부분 문제를 해결해 전체 문제를 해결**할 수 있게 해준다.

> 📝 내 코드 `04_07`은 저장할 때 `memo[n] = nth_fibo`(전역 변수)를 쓰고 있다.
> PDF처럼 파라미터 `fibo_memo[n]`에 저장해야 다른 dict를 넘겨도 동작한다.

| | 재귀 | DP (메모이제이션) |
|---|---|---|
| 같은 값 재계산 | 매번 다시 계산 | 한 번만 계산 후 재사용 |
| 시간 복잡도 | 약 O(2^N) | O(N) |

---

## 6. 숙제

### Q1. 농심 라면 공장 → **힙** (`04_08`)

**문제**: 하루에 밀가루 1톤 사용. k일 이후에야 원래 공장에서 공급받을 수 있다.
현재 재고 `stock`, 공급 날짜 `dates`, 공급량 `supplies`, `k`가 주어질 때, 밀가루가 떨어지지 않게 하는 **최소 공급 횟수**는?

```
stock = 4, dates = [4, 10, 15], supplies = [20, 5, 10], k = 30
→ 26개가 필요 → 20, 10을 가져오면 됨 → 2번
```

**함정**: 무조건 큰 것부터 가져오면 안 된다.

```
stock = 2, dates = [1, 10], supplies = [10, 100], k = 11
→ 10일의 100톤을 기다리다간 2일째에 재고가 바닥남
```

**핵심 아이디어**
- 목표: **재고가 바닥나기 전까지 받을 수 있는 밀가루 중 제일 많은 것**을 받는다.
- 재고 상태에 따라 후보가 **동적으로 바뀌고**, 그중 **최댓값만** 꺼내면 된다. → **힙(heapq)**
- `stock`이 `k`보다 많아질 때까지 반복
- 재고로 버틸 수 있는 날짜(`dates[i] <= stock`)의 공급량을 힙에 넣고, 최댓값을 꺼내 `stock`에 더한다.
- `last_added_date_index`로 이미 넣은 날짜를 기억해 **중복으로 넣지 않는다.**

<details>
<summary>답안 코드 (직접 풀어본 뒤 펼치기)</summary>

```python
import heapq

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer

print(get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))          # 2
print(get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))  # 4
print(get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))               # 1
```

</details>

### Q2. 샤오미 로봇 청소기 → **BFS**

**문제**: N×M 방(0 빈칸, 1 벽)에서 로봇 청소기가 아래 규칙으로 움직일 때 **청소하는 칸의 개수**는?
위치 `(r, c)`, 방향 `d` (0 북, 1 동, 2 남, 3 서)

1. 현재 위치를 청소한다.
2. 현재 방향 기준 **왼쪽 방향부터** 차례대로 탐색한다.
   - a. 왼쪽에 청소 안 한 칸이 있으면 → 그 방향으로 회전 후 한 칸 전진, 1번부터
   - b. 없으면 → 그 방향으로 회전만 하고 2번으로
   - c. 네 방향 모두 청소했거나 벽이면 → 방향 유지한 채 **한 칸 후진**, 2번으로
   - d. c인데 뒤가 벽이라 후진도 못하면 → **멈춤**

**핵심 아이디어**
- 갈 수 있는 모든 칸을 탐색 → **BFS**
- 방문 기록은 2차원 맵에 직접: **0 청소 안 함 / 1 벽 / 2 청소함**
- 방향을 배열로 정의:

```python
#     북  동  남  서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
```

| 동작 | 공식 | 예시 |
|---|---|---|
| 왼쪽으로 회전 | `(d + 3) % 4` | 북(0) → 서(3), 동(1) → 북(0) |
| 후진 방향 | `(d + 2) % 4` | 북(0) → 남(2), 동(1) → 서(3) |

<details>
<summary>답안 코드 (직접 풀어본 뒤 펼치기)</summary>

```python
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4

def get_d_index_when_go_back(d):
    return (d + 2) % 4

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])
    count_of_departments_cleaned = 1
    room_map[r][c] = 2
    queue = deque([[r, c, d]])

    while queue:
        r, c, d = queue.popleft()
        temp_d = d
        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            # a
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2
                queue.append([new_r, new_c, temp_d])
                break

            # c
            elif i == 3:
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                queue.append([new_r, new_c, d])

                # d
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned

# 예제 맵(7, 4, 0) → 57
```

</details>

### Q3. CGV 극장 좌석 자리 구하기 → **DP**

**문제**: 1~N번 좌석, 자기 좌석 또는 **바로 왼쪽/오른쪽**으로만 옮길 수 있다. VIP는 **자기 자리에 고정**.
좌석 수와 VIP 좌석 번호가 주어질 때 **앉는 방법의 가짓수**는?

```
seat_count = 9, vip_seat_array = [4, 7]  → 12
```

**핵심 아이디어**
- VIP 좌석으로 구역이 나뉜다: `[1 2 3] 4 [5 6] 7 [8 9]`
- 구역 길이별 경우의 수를 써보면 규칙이 보인다:

| 좌석 수 | 경우의 수 |
|---|---|
| 1 | 1 |
| 2 | 2 (`12`, `21`) |
| 3 | 3 (`123`, `213`, `132`) |
| 4 | 5 |
| 5 | 8 |

→ **피보나치 수열**! 단, `F(1) = 1, F(2) = 2`로 시작

**왜 피보나치?** n번째 좌석에 앉는 방법은 두 가지
1. n번 티켓이 그대로 앉음 → 나머지 **n-1개**를 배치 → `F(n-1)`
2. n-1번 티켓이 n번에 앉음 → n번 티켓은 반드시 n-1번에 앉아야 함 → 나머지 **n-2개** 배치 → `F(n-2)`

→ `F(N) = F(N-1) + F(N-2)`

**구역마다 경우의 수를 구해 곱한다 (곱의 법칙)**: `F(3) × F(2) × F(2) = 3 × 2 × 2 = 12`

<details>
<summary>답안 코드 (직접 풀어본 뒤 펼치기)</summary>

```python
memo = {
    1: 1,   # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways

print(get_all_ways_of_theater_seat(9, [4, 7]))      # 12
print(get_all_ways_of_theater_seat(9, [2, 4, 7]))   # 4
print(get_all_ways_of_theater_seat(11, [2, 5]))     # 26
print(get_all_ways_of_theater_seat(10, [2, 6, 9]))  # 6
```

> VIP가 붙어 있거나(예: `[3, 4]`) 맨 끝 좌석이 VIP면 구역 길이가 0이 되는데, `memo`에 `0: 1`이 없으면 무한 재귀가 난다.
> 안전하게 하려면 `memo = {0: 1, 1: 1, 2: 2}` 로 시작하면 된다. (빈 구역은 앉는 방법 1가지)

</details>

---

## 7. 한눈에 정리

| 상황 | 쓸 것 |
|---|---|
| 항상 최댓값/최솟값이 필요하고 삽입·삭제가 잦다 | **힙** (`heapq`, 최대 힙은 `-1` 곱하기) |
| 모든 경로를 끝까지 탐색 / 공간을 아껴야 한다 | **DFS** (재귀 or 스택) |
| 최단 거리, 최소 횟수 / 가까운 것부터 | **BFS** (큐, `deque`) |
| 같은 하위 문제가 반복해서 등장한다 | **DP** (메모이제이션) |
| 2차원 맵에서 방향 이동 | `dr`, `dc` 배열 + `(d + 3) % 4` 회전, `(d + 2) % 4` 후진 |
