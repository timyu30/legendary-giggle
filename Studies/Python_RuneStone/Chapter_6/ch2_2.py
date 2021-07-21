def search(lst, value):
    if lst.get_head() == None:
        return False
    node = lst.get_head()
    while node.next_element:
        if node.data == value:
            return True
        node = node.next_element
    return False