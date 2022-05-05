from os import sep

class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to reverse the linked list
	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	# Function to insert a new node at the beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def reorder(self):
		print(self.head.data)
		slow=self.head
		fast=self.head.next
		
		while fast and fast.next:
			slow=slow.next
			fast=fast.next.next
		print(slow.data,fast.data)

		second=slow.next
		prev=slow.next=None

		while second:
			tmp=second.next
			prev=second
			second=tmp

			#merge
			first,second=self.head,prev
			while second:
				tmp1,tmp2=first.next,second.next
				first.next=second
				second.next=tmp1
				first,second=tmp1,tmp2


	# Utility function to print the linked LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print (temp.data,end=" ")
			temp = temp.next


# Driver code
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()
llist.reorder()

