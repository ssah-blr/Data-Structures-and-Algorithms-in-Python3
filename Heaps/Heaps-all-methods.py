# Python List based Heap. Root node at index 0.

class MaxHeap():
    def __init__(self):
        self.max_heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.max_heap[index1], self.max_heap[index2] = self.max_heap[index2], self.max_heap[index1]

    def insert(self,value): # Insert at last of Heap. Move it towards root, untill it is at root or as correct parent
        self.max_heap.append(value)
        current = len(self.max_heap) - 1

        while current > 0 and self.max_heap[current] > self.max_heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)

    def sink_down(self,index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.max_heap) and self.max_heap[max_index] < self.max_heap[left_index]):
                max_index = left_index

            if (right_index < len(self.max_heap) and self.max_heap[max_index] < self.max_heap[right_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index,max_index)
                index = max_index
            else:
                return False

    def remove(self):
        if len(self.max_heap) == 0:
            return None
        
        if len(self.max_heap) == 1:
            return self.max_heap.pop()
        
        max_value = self.max_heap[0]
        self.max_heap[0] = self.max_heap.pop() # Replace the last Iteam at top, trigger sink_down to rebalance the Heap
        self.sink_down(0)

        return max_value


myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.max_heap)

myheap.remove()
print(myheap.max_heap)

myheap.remove()
print(myheap.max_heap)
