class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertNode(self,data):
        if self.head is None:
            self.head=Node(data)

        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode

    def printLinkedList(self):
        nodes=self.head

        while nodes is not None:
            print(nodes.data,end="--->")
            nodes=nodes.next 

    def removeFromMiddle(self):
        total_element=0
        currNode=self.head
        
        while currNode is not None:
            total_element +=1
            currNode=currNode.next
        
        middle_element=total_element//2
        
        count=0
        node=self.head

        while node is not None:
            if count==middle_element:
                node=node.next
            print(node.data,end="-->")
            count +=1
            node =node.next





l1=LinkedList()
# l1.insertNode(5)
# l1.insertNode(4)
l1.insertNode(3)
l1.insertNode(2)
# l1.insertNode(1)
# l1.printLinkedList()
l1.removeFromMiddle()