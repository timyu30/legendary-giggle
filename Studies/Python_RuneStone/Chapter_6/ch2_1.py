def insert_at_tail(lst, value):
    #lst.print_list()
    new_node = Node(value)
    
    if lst.is_empty():
        lst.head_node = new_node
        return lst

    node = lst.get_head()
    while node.next_element is not None:
        node = node.next_element
    
    node.next_element = new_node
    return lst