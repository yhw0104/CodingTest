class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        count = self.count() + 1    # 총 개수 - 1
        get_node_index = count - k
        cur = self.head
        for i in range(get_node_index):
            cur = cur.next

        return cur
    

    def count(self):
        count = 0
        cur = self.head
        while cur.next is not None:
            count += 1
            cur = cur.next

        return count

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!