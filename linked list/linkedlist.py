class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,data):
        if self.head ==None:
            newNode=Node(data)
            self.head=newNode
        
    def printList(self):
        print(self.head.data)

ll=LinkedList()
ll.insert(5)
print(ll.printList())












data=[1,2,3]