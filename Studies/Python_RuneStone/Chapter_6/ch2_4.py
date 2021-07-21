from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Node class attributes: {data, next_element}


def length(lst):
    if lst.is_empty():
        return 0
    node = lst.get_head()
    count = 0
    while node:
        count = count + 1
        node = node.next_element
    return count

next = current.next #save the next address
current.next = prev #change current to point back
prev = current #set prev to the current node
current = next #change current to saved next address

def recurseRev(lst):
    if lst.head == null:
        return
    
    

