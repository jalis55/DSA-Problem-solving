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

def inOrder(root):
    if root is None:
        return

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def preOrder(root):
    if root is None:
        return 
    
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data)

def serachBST(root,val):
    if root is None:
        return 
    else:
        if root.data==val:
            return "found"
        elif root.data>val:
            serachBST(root.left,val)
        else:
            serachBST(root.right,val)
def sumBst(root):
    if root is None:
        return 0
    
    return root.data+sumBst(root.left)+sumBst(root.right)

tree=Node(10)
tree.insert(30)
tree.insert(5)
print(preOrder(tree))
# print(sumBst(tree))





# # inOrder(tree)
# preOrder(tree)
# # postOrder(tree)

# print(serachBST(tree,2))