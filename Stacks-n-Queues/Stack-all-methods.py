# Constructor for New Node of Stack
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            temp = self.top
            new_node.next = temp
            self.top = new_node
        self.height += 1
        return True

    def stack_print(self):
        temp = self.top
        while temp is not None:
            print(temp.value,end=' ')
            temp = temp.next
        print('')

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value
    
    def get_height(self):
        return self.height


# Use and Examples of Methods for Stack Push, Print, Pop

S1 = Stack(4)
S1.push(6)
S1.push(7)
S1.push(8)
S1.push(5)
S1.stack_print()
print(' Pop:',S1.pop())
print(' Pop:',S1.pop())
S1.stack_print()
print(' Stack Height:',S1.get_height())