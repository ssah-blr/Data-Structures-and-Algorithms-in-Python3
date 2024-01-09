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
    
    def DFS_Pre_order(self): # Depth First Search - Pre Order
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
        
    def DFS_Post_order(self): # Depth First Search - Post Order
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)
        return results

    def DFS_In_order(self): # Depth First Search - In Order
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results


BST = BinarySearchTree()
BST.insert(47)
BST.insert(21)
BST.insert(76)
BST.insert(18)
BST.insert(27)
BST.insert(52)
BST.insert(82)

print(BST.root.value)
print(BST.root.left.value)
print(BST.root.right.value)
print(BST.contains(4))
print(BST.contains(1))

print(BST.DFS_Pre_order())
print(BST.DFS_Post_order())
print(BST.DFS_In_order())

