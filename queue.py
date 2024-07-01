class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        print_value = ""
        temp = self.first
        while temp is not None:
            print_value += f" {temp.value} <-"
            temp = temp.next
        print(print_value)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.first
        before = None
        self.last = self.first

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        self.first = before

queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()
queue.reverse()
queue.print_queue()