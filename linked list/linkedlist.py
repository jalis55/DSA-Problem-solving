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
    def inserTail(self,data):
        if self.head==None:
            self.insert(data)
        else:
            newNode=Node(data)
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode


    def removeItem(self,data):
        if self.head == None:
            return "Empty"
        if self.head.data==data:
            self.head=self.head.next
            return 
        temp=self.head
        curr=temp
        while temp:
            if temp.data==data:
                curr.next=temp.next
                return "Item removed"
            else:
                curr=temp
                temp=temp.next
        else:
            return "Data not found"
        


    def lastItem(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        return temp.data
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

print(ll.lastItem())
ll.inserTail(66)
print(ll.printList())
ll.removeItem(13)
print(ll.printList())
print(ll.removeItem(7))
# print(ll.printList())


