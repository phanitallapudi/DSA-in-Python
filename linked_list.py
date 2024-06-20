class ListNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val):
        new_node = ListNode(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        lst = ""
        while temp is not None:
            lst += f"{temp.value} "
            temp = temp.next
        return lst
    
    def add(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def padd(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.length -= 1
        self.tail = pre
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def ppop(self):
        if self.length == 0:
            return None
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return True
    
    def get(self, index):
        if self.length == 0:
            return None
        if self.length < index:
            return None
        count = 0
        temp = self.head
        while temp is not None:
            if count == index:
                return temp
            temp = temp.next
            count += 1
        return None
    
    def get_index(self, value):
        count = 0
        location = None
        if self.length == 0:
            return None
        temp = self.head
        while temp is not None:
            if temp.value == value:
                location = count
            count += 1
            temp = temp.next
        return location

    def set_value(self, index, value):
        temp = self.get(index=index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = ListNode(val=value)
        if self.length == 0:
            self.length = 1
            self.head = new_node
            self.tail = new_node
            return True
        if self.length <= index:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
        temp = self.get(index=index)
        if temp is not None:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.ppop()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
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
            before = temp
            temp = after
        
        return before
    
    def middlenode(self):
        length = int(self.length / 2)
        middle_node = self.get(index=length)
        return middle_node.value if middle_node else None
