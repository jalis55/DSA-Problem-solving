class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,data):
        if self.head ==None:
            self.head=Node(data)
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
        
    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next


ll=LinkedList()
ll.insert(5)
ll.insert(2)
print(ll.printList())












data=[1,2,3]