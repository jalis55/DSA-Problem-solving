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

def printLinkedList(head):
    nodes=head

    while nodes is not None:
        print(nodes.data,end="--->")
        nodes=nodes.next 

def removeDuplicate(head):
    dummy=head
    prev=dummy.data

    curr=dummy.next

    if not curr:
        return dummy
    while curr:
        print(curr.data)
        if curr.data==prev:
            
            curr=curr.next
        else:
            dummy.next=curr
            print(dummy.next.data)
            prev=curr.data
            curr=curr.next
    dummy.next=None
    return head

    


l1=LinkedList()
# l1.insertNode(5)
# l1.insertNode(4)
l1.insertNode(3)
l1.insertNode(2)
l1.insertNode(1)
l1.insertNode(1)
# l1.printLinkedList()

d=removeDuplicate(l1.head)

printLinkedList(d)