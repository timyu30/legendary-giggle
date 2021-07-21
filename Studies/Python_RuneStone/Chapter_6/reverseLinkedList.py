# Python3 implementation of the approach
import math

# Link list node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to reverse the linked list in groups of
#size k and return the poer to the new head node.
def reverse(head, k) :
	prev = None
	curr = head
	temp = None

    
	tail = None
	newHead = None
	join = None
	t = 0

	# Traverse till the end of the linked list
	while (curr) :
		t = k
		join = curr
		prev = None

		# Reverse group of k nodes of the linked list
		while (curr and t > 0):
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
            
			t = t - 1

		# Sets the new head of the input list
		if (newHead == None):
			newHead = prev

		# Tail pointer keeps track of the last node
		# of the k-reversed linked list. We join the
		# tail poer with the head of the next
		# k-reversed linked list's head
		if (tail != None):
			tail.next = prev

		# The tail is then updated to the last node
		# of the next k-reverse linked list
		tail = join
	
	# newHead is new head of the input list */
	return newHead

# Function to insert a node at
# the head of the linked list
def push(head_ref, new_data) :
	
	# allocate node */
	new_node =Node(new_data)

	# put in the data */
	new_node.data = new_data

	# link the old list off the new node */
	new_node.next = head_ref

	# move the head to po to the new node */
	head_ref = new_node
	return head_ref

# Function to print the linked list
def prList(node):
	while (node != None) :
		print(node.data, end = " ")
		node = node.next
	
# Driver code
if __name__=='__main__':

	# Start with the empty list
	head = None

	# Created Linked list is
	# 1.2.3.4.5.6.7.8.9
	head = push(head, 9)
	head = push(head, 8)
	head = push(head, 7)
	head = push(head, 6)
	head = push(head, 5)
	head = push(head, 4)
	head = push(head, 3)
	head = push(head, 2)
	head = push(head, 1)

	k = 3

	print("Given linked list ")
	prList(head)
	head = reverse(head, k)

	print("\nReversed Linked list ")
	prList(head)

# This code is contributed by Srathore
