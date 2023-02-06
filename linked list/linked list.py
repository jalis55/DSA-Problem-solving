class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        if self.head is not None:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
        else:
            self.head=Node(data)
    def delNode(self):
        if self.head is not None:
            temp=self.head
            self.head=temp.next
        else:
            print("\nNothing to delete")
    
    def lastNode(self):
        if self.head is None:
            print("Empty Linked list")
        elif self.head.next ==None:
            self.head=None
        else:
            second_last_node=self.head
            while second_last_node.next.next !=None:
                second_last_node=second_last_node.next
            second_last_node.next=None
    def insertTail(self,data):
        if self.head is not None:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            newNode=Node(data)
            curr.next=newNode
        else:
            newNode=Node(data)
            self.head=newNode
    def reverse(self):
        prev=None
        curr=self.head
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def reverseKgroup(self,head,k):
        curr=head
        next=None
        prev=None
        count=0

        while curr is not None and count < k:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count +=1
        if next is not None:
            head.next=self.reverseKgroup(next,k)
        return prev



    def listprint(self):
        if self.head is None:
            print("Empty")
        printval = self.head
        while printval is not None:
            print (printval.data,end="->")
            printval = printval.next



ll=LinkedList()

data=[1,2,3]
for i in data:
    ll.insert(i)

# ll.insert(1)

# ll.lastNode()
ll.listprint()
