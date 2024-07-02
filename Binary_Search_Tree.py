class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while True:
            if value == temp.value:
                return True
            if value < temp.value:
                if temp.left is None:
                    return False
                temp = temp.left
            else:
                if temp.right is None:
                    return False
                temp = temp.right
        return False
    
    def sum_nodes(self, node):
        if node is None:
            return 0
        leftSum = self.sum_nodes(node.left)
        rightSum = self.sum_nodes(node.right)
        return node.value + leftSum + rightSum
    
    def sum_recursion(self):
        return self.sum_nodes(self.root)
    
    def sum_traversal(self):
        if self.root is None:
            return 0
        stack = [self.root]
        total_sum = 0
        while stack:
            node = stack.pop()
            if node is not None:
                total_sum += node.value
                stack.append(node.left)
                stack.append(node.right)
        return total_sum
