from tkinter.messagebox import NO


class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None
    def listprint(self):

        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next


n1=Node(1)
ll=LinkedList()
ll.head=n1

n2=Node(2)
n1.next=n2

n3=Node(3)
n2.next=n3
ll.listprint()

