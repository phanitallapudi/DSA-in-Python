class Node(object):
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            next_node = temp.next.value if temp.next else None
            prev_node = temp.prev.value if temp.prev else None
            print(f"current node: {temp.value}, next node: {next_node}, previous node: {prev_node}")
            temp = temp.next
        print("\n")

    def add(self, value):
        new_node = Node(val=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def padd(self, value):
        new_node = Node(val=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        temp = self.tail 
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def ppop(self):
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        temp.next = None
        return temp
    
    def get(self, index):
        count = 0
        temp = self.head
        while temp is not None:
            if index == count:
                return temp
            temp = temp.next
            count += 1
        return None
    
    def set(self, index, value):
        if self.length == 0:
            return None
        count = 0
        temp = self.head
        while temp is not None:
            if index == count:
                temp.value = value
                return temp
            temp = temp.next
            count += 1
        return None
    
    def insert(self, index, value):
        new_node = Node(val=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True
        count = 0
        temp = self.head
        while temp is not None:
            if index == count:
                next_node = temp.next
                new_node.next = next_node
                new_node.prev = temp
                temp.next = new_node
                self.length += 1
                return temp
            temp = temp.next
            count += 1
        return None
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.ppop()
        if index == self.length - 1:
            return self.pop() 
        temp = self.get(index=index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        before = None
        after = temp.next
        while temp:
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after
