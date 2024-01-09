class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self,value):
        newnode = Node(value)
        self.first = newnode
        self.last = newnode
        self.length = 1

    def Enqueue(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.first = newnode
        else:
            self.last.next = newnode
            self.last = newnode
        self.length += 1
        return True
    
    def Print_Queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print('')

    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp.value
        
    
Q1 = Queue(2)
Q1.Enqueue(4)
Q1.Enqueue(5)
Q1.Enqueue(7)
Q1.Print_Queue()
print(' Dequeue:',Q1.Dequeue())
Q1.Print_Queue()
