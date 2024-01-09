# Constructor for New Node class of Doubly Linked List
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

# Methods for Constructor, Print List, Append, Pop, Prepend, Pop_first, get, set, insert, remove
class DoublyLinkedList():
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
        print('')

    def append(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        self.tail.next = None
        self.length -= 1
        return temp.value
    
    def prepend(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            temp = self.head
            newnode.next = temp
            temp.prev = newnode
            self.head = newnode
        self.length += 1        
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        value = temp.value
        if self.length == 1:            
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None
            self.length -= 1
        return value
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):           
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def get_value(self,index):
        return self.get(index).value
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        newnode = Node(value)
        before = self.get(index-1)
        after = before.next

        before.next = newnode
        after.prev = newnode
        newnode.prev = before
        newnode.next = after

        self.length += 1
        return True
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.popfirst()
        if index == self.length:
            return self.pop()
        
        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None

        self.length -= 1
        return True

        

DLL = DoublyLinkedList(3)
DLL.append(5)
DLL.append(7)
DLL.append(10)
DLL.append(9)
DLL.append(15)

DLL.printList()
print(' Pop',DLL.pop())
DLL.printList()

print(' Perpend')
DLL.prepend(6)
DLL.printList()

print(' Pop First',DLL.popfirst())
DLL.printList()

print(' Get Index 2:',DLL.get_value(2))
DLL.printList()

print(' Set Index 3, Value 8')
DLL.set_value(3,8)
DLL.printList()

print(' Insert Index 2, Value 11')
DLL.insert(2,11)
DLL.printList()

print(' Remove Index 3')
DLL.remove(3)
DLL.printList()
