
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self, value):
        self.head = Node(value)

    # 맨 뒤에 값 추가
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    # 노드 전체 print
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # value 값으로 몇번째 노드에 있는지 찾기
    def find_by_value(self, value):
        cur = self.head
        count = 1
        while cur is not None:
            if cur.data == value:
                print(value, "는 ", count, "번째 노드에 있습니다.")
            cur = cur.next
            count += 1

    # index 값으로 data 값 찾기
    def find_by_index(self, index):
        cur = self.head

        count = self.find_max_index()
        
        if count < index:
            print("인덱스를 넘어갔습니다.")
            return 1
        
        for i in range(index):
            cur = cur.next

        return cur
        # print(index, "번째 인덱스에는", cur.data, "의 값이 있습니다.")

    # 노드 index의 max값 찾기
    def find_max_index(self):
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1

        return count-1

    # index 자리에 원하는 value 넣기
    def add_node(self, index, value):
        add = Node(value)
        cur = self.head

        # index파라미터가 0일때 헤드에 value값이 들어가야됨
        if index == 0:
            add.next = cur
            self.head = add
            return self.print_all()
        
        for i in range(index-1):
            cur = cur.next

        add.next = cur.next
        cur.next = add

 
        return self.print_all()

    # index자리의 data 삭제
    def remove_node(self, index):
        # index 파라미터가 0일경우
        if index == 0:
            self.head = self.head.next
            return 1 

        # index 파라미터가 max값일 경우
        max = self.find_max_index()
        # print(max)
        if index == max:
            self.find_by_index(index-1).next = None
            return 1

        if index> max:
            return print("index값을 넘어갔습니다.")

        prev_node = self.find_by_index(index-1)
        front_node = self.find_by_index(index+1)

        prev_node.next = front_node



# ["기관실"] -> ["시멘트"] -> ["자갈"] -> ["밀가루"] -> ["우편"]

node1 = Linked_List("기관실")
node1.append("시멘트")
node1.append("자갈")
node1.append("밀가루")
node1.append("우편")

# node1.find_by_value("밀가루")
# node1.find_by_value("시멘트")

# print(node1.find_by_index(4).data)

# node1.add_node(0, "하연")

node1.remove_node(2)
node1.print_all()