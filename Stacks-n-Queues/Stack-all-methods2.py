# Stack Using Python List
class Stack():
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def stack_print(self):
        print(self.items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

# Use and Examples of Methods for Stack Push, Print, Pop, Peek, isEmpty

S2 = Stack()
S2.push(3)
S2.push('Hello')
S2.push(6)
S2.push('Six')
S2.stack_print()
print(' Pop:',S2.pop())
S2.stack_print()
print(' Peek:',S2.peek())
print(' IsEmpty',S2.isEmpty())
print(' Size',S2.size())
