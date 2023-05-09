class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data


# Print the tree


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
def Inorder(root):
        if root:
            Inorder(root.left)
            print(root.data)
            Inorder(root.right)
def PreOrder(root):
    if root:
        print(root.data)
        PreOrder(root.left)
        PreOrder(root.right)

def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data)

def sum_left_subtree(root):
    if root is None:
        return 0
    return root.data+sum_left_subtree(root.left)

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print("--------Inorder----------")
Inorder(root)
print("--------PreOrder----------")
PreOrder(root)
print("--------PostOrder----------")
PostOrder(root)
print(sum_left_subtree(root.left))