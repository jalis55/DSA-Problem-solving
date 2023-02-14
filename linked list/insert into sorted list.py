import random


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:

            temp = self.head
            prev = None
            while temp:
                if temp.data > data:

                    newNode = Node(data)
                    self.head = newNode
                    newNode.next = temp
                    temp = temp.next
                else:

                    # newNode = Node(data)
                    # newNode.next = self.head
                    # self.head = newNode

    def printList(self):
        if self.head is None:
            print("Empty")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


ll = LinkedList()
ll.insert(3)
ll.insert(1)

print(ll.printList())
