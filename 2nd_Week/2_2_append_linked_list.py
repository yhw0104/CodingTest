
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self, value):
        self.head = Node(value)
 
    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            
    def find(self, value):
        cur = self.head
        count = 1
        while cur is not None:
            if cur.data == value:
                print(value, "는 ", count, "번째 노드에 있습니다.")
            cur = cur.next
            count += 1
                


# ["기관실"] -> ["시멘트"] -> ["자갈"] -> ["밀가루"] -> ["우편"]
# 3을 가진 Node 를 만드려면 아래와 같이 하면 됩니다!
# node = Node(3) # 현재는 next 가 없이 하나의 노드만 있습니다. [3]

node1 = Linked_List("기관실")
node1.append("시멘트")
node1.append("자갈")
node1.append("밀가루")
node1.append("우편")

node1.find("밀가루")
node1.find("시멘트")