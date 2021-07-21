def delete(lst, value):
    #var to hold prev and current nodes
    
    prev_node = lst.get_head()
    current_node = lst.get_head()
    deleted = False
    #search through the lst for value
    while current_node:
        if current_node.data == value:
            prev_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            return deleted
        current_node = current_node.next_element
    
    return deleted