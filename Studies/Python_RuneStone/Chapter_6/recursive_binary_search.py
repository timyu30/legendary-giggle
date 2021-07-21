"""Binary Search but recursively
This algorithm is a great example of 
divide and conquer strategy. The smaller 
pieces of the problem is reassembled to     
the whole problem.
The recursion occurs on either half of the
list.
"""
def binary_search_rec(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list)//2
        if a_list[midpoint] == item:
            return True
        elif a_list[midpoint] > item:
            return binary_search_rec(a_list[:midpoint], item)
        else:
            return binary_search_rec(a_list[midpoint+1:], item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print(test_list[:1-1])

#print(binary_search_rec(test_list, 3))
#print(binary_search_rec(test_list, 13))
#print(binary_search_rec(test_list, 42))