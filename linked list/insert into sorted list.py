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
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def printList(self):
        if self.head is None:
            print("Empty")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


random.seed(5)
lst = [random.randint(1, 20) for i in range(3)]
print(lst)
ll = LinkedList()
for i in random.sample(lst, 3):
    ll.insert(i)

print(ll.printList())
