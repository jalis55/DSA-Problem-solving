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




    def removeNth(self):
        if self.head is None:
            return False
        count=0
        temp=self.head
        while temp:
            count +=1
            temp=temp.next
        
        flag=count-2
        temp2=self.head
        while temp2:
            if flag==count:
                temp2=temp2.next.next
                print(temp2.data)
                break
            else:
                count -=1
                temp2=temp2.next
        while temp2:
            print(temp2.data)
            temp2=temp2.next
        self.head=temp2
        


    def listprint(self):
        if self.head is None:
            print("Empty")
        printval = self.head
        while printval is not None:
            print (printval.data,end="->")
            printval = printval.next



ll=LinkedList()

data=[1,2,3,4,5]
for i in data:
    ll.insert(i)

# ll.insert(1)

# ll.lastNode()
# ll.listprint()
ll.removeNth()
