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

def max_in_bst(root):
    if root is None:
        return (-12121212)
    left_max=max_in_bst(root.left)
    right_max=max_in_bst(root.right)
    return max(root.data,left_max,right_max)

def min_in_bst(root):
    if root is None:
        return (434343)
    left_min=min_in_bst(root.left)
    right_min=min_in_bst(root.right)
    return min(root.data,left_min,right_min)



# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(72)
root.PrintTree()
print("--------Inorder----------")
Inorder(root)
print("--------PreOrder----------")
PreOrder(root)
print("--------PostOrder----------")
PostOrder(root)
print(f'Max element is:{max_in_bst(root)}')
print(f'Min element is:{min_in_bst(root)}')