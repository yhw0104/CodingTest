# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오. 

# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.

# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

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

    def get_max_index(self):
        cur = self.head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next      

        return count-1

def get_linked_list_sum(linked_list_1, linked_list_2):

    list1_max_index = linked_list_1.get_max_index()
    list2_max_index = linked_list_2.get_max_index()

    cur1 = linked_list_1.head
    cur2 = linked_list_2.head
    cur1_num = 0
    cur2_num = 0

    for i in range(list1_max_index, -1, -1):
        num = cur1.data * (10 ** i)        
        cur1_num += num
        cur1 = cur1.next


    for i in range(list2_max_index, -1, -1):
        num = cur2.data * (10 ** i)        
        cur2_num += num
        cur2 = cur2.next


    return (cur1_num + cur2_num)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)


linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
