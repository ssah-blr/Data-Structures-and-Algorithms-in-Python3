# Constructor for New Node class of Linked List
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Methods for Constructor, Print List, Append, Pop, Prepend, Pop_first, get, set, insert, remove
class LinkedList():
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print('')

    def append(self, value):
        newnode = Node(value)
        if self.head == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        #return(True)

    def pop(self):
        if self.length == 0:
            return None        
        pre = self.head
        temp = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value    

    def prepend(self, value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode        
        self.length += 1

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def get_value(self,index):
        return self.get(index).value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new = Node(value)
        temp = self.get(index - 1)
        new.next = temp.next
        temp.next = new
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


LL = LinkedList(1)
LL.append(2)
LL.append(3)
LL.append(5)
LL.append(7)
LL.append(9)
LL.printlist()
print(' Pop:',LL.pop())
LL.prepend(8)
print(' Prepend: 8')
LL.printlist()
print(' Popfirst:',LL.popfirst())
LL.printlist()
print(' Get Index 3:',LL.get_value(3))
print(' Set Index 3 to Value 4',LL.set_value(3,4))
LL.printlist()
print(' Set Index 3 the Value 11',LL.insert(3,11))
LL.printlist()
print(' Remove Index 3',LL.remove(3))
LL.printlist()
LL.reverse()
print(' Reverse')
LL.printlist()

