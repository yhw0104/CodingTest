class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        index = len(self.items) - 1
        while index > 1:
            parent = index // 2
            if self.items[parent] < self.items[index]:
                self.items[parent], self.items[index] = self.items[index], self.items[parent]
                index = parent
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!