def sequential_search(a_list, item):
    length = len(a_list)
    pos = 0
    while pos < length:
        if a_list[pos] == item:
            return True
        pos = pos + 1
    return False

def ordered_sequential_search(a_list, item):
    length = len(a_list)
    pos = 0
    while pos < length:
        if a_list[pos] == item:
            return True
        elif a_list[pos] > item:
            return False
        pos = pos + 1
    return False

test_list= [0, 1, 2, 3, 7, 8, 10]

print(ordered_sequential_search(test_list, 7))

print(ordered_sequential_search(test_list, -3))