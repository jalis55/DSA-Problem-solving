import random
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

    def reverseList(self):
        if self.head==None:
            return
        else:
            temp=self.head
            prev=None
            while temp:
                next=temp.next
                temp.next=prev
                prev=temp
                temp=next
            self.head=prev
        return

    def printList(self):
        if self.head is None:
            print("Empty")
        temp = self.head
        while temp is not None:
            print (temp.data,end="->")
            temp = temp.next

random.seed(2)
lst=[random.randint(1,20) for i in range(20)]
ll=LinkedList()
for i in random.sample(lst,5):
    ll.insert(i)


print(ll.printList())
print(ll.reverseList())
# print(ll.printList())