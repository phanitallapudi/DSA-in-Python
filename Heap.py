class Heap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        parent_index = self.get_parent_index(current_index)
        
        while current_index > 0 and self.heap[current_index] > self.heap[parent_index]:
            self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
            current_index = parent_index
            parent_index = self.get_parent_index(current_index)
    
    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        current = 0
        
        while True:
            left_child_index = (current * 2) + 1
            right_child_index = (current * 2) + 2
            largest = current

            if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest == current:
                break
            
            self.heap[current], self.heap[largest] = self.heap[largest], self.heap[current]
            current = largest
        
        return max_item
    
    def print_heap(self):
        return self.heap
    