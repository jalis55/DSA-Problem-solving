# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class Node:
    def __init__(self,data=0,next=None) -> None:
        self.data=data
        self.next=next


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
        if self.head is None:
            print("Empty")
        temp = self.head
        while temp is not None:
            print (temp.data,end="->")
            temp = temp.next


def margeList(l1,l2):
    marged_list=Node()
    head=marged_list
    while l1 and l2:
        if l1.data <l2.data:
            head.next=l1
            l1=l1.next
        else:
            head.next=l2
            l2=l2.next
        head=head.next
    if l1:
        head.next=l1
    else:
        head.next=l2
    return marged_list


l1=LinkedList()

l1.insert(3)
l1.insert(2)
l1.insert(1)
print(l1.printList())

l2=LinkedList()
l2.insert(5)
l2.insert(4)
l2.insert(1)
print(l2.printList())

marged=margeList(l1.head,l2.head)

while marged:
    print(marged.data,end="-->")
    marged=marged.next

