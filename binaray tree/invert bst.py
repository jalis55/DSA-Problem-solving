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

def invert_bst(root):
    if root is None:
        return None
    root.left,root.right=root.right,root.left
    invert_bst(root.left)
    invert_bst(root.right)
    return root
inputs = [4,2,7,1,3,6,9]

# Use the insert method to add nodes
root = Node(inputs[0])
for i in inputs[1:]:
    root.insert(i)

print("--------Inorder----------")
Inorder(root)

print("-----------after invert------------")
invert_bst(root)

Inorder
