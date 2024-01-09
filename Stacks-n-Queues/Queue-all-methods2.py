# Queue Using Python List

class Queue():
    def __init__(self):
        self.items = []

    def Enqueue(self,value):
        self.items.insert(0,value)

    def Print_Queue(self):
        print(self.items)

    def Dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


Q2 = Queue()
Q2.Enqueue(4)
Q2.Enqueue(5)
Q2.Enqueue(7)
Q2.Print_Queue()
print(' Dequeue:',Q2.Dequeue())
Q2.Print_Queue()
print(' isEmpty',Q2.isEmpty())
print(' Size',Q2.size())
