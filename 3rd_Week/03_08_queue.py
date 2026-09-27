class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        dequeue = self.head.data
        self.head = self.head.next
        return dequeue

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(7)
queue.dequeue() 
print(queue.peek())
queue.dequeue()
queue.dequeue()
print(queue.peek())