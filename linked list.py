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

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next



ll=LinkedList()


data=list(range(1,21,3))

for i in data:
    ll.insert(i)

ll.listprint()

