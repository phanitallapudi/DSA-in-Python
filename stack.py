class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value=None) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value
    
    def reverse(self):
        before = None
        temp = self.top

        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        self.top = before

    def print_stack(self):
        print_value = ""
        temp = self.top
        while temp is not None:
            print_value += f"{temp.value} -> "
            temp = temp.next
        if print_value:
            print(print_value)
        else:
            print("Stack is empty")