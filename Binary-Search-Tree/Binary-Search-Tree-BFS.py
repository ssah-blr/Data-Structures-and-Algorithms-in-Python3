class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
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
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False
    
    def BFS(self): # Breath First Search
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0 :
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return results


BST = BinarySearchTree()
BST.insert(8)
BST.insert(4)
BST.insert(10)
BST.insert(2)
BST.insert(5)
BST.insert(9)
BST.insert(11)

print(BST.root.value)
print(BST.root.left.value)
print(BST.root.right.value)
print(BST.contains(4))
print(BST.contains(1))

print(BST.BFS())

