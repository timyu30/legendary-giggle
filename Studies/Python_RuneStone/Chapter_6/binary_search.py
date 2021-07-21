"""Binary Search of Ordered List"""

#%%
def binary_search(a_list, item):
    #middle = len(a_list)/2
    start = 0
    end = len(a_list) -1
    while start <= end:
        middle = (start + end)//2
        mid = a_list[middle]
        #print(f'value: {mid}, start: {start}, end: {end}')
        if mid == item:    
            return True
        elif mid > item:
            end = middle -1
        elif mid < item:
            start = middle +1
    return False

# def binary_search(a_list, item):
#     first = 0
#     last = len(a_list) - 1

#     while first <= last:
#         midpoint = (first + last) // 2
#         if a_list[midpoint] == item:
#             return True
#         elif item < a_list[midpoint]:
#             last = midpoint - 1	        
#         else:
#             first = midpoint + 1

#     return False

    
test_list= [0, 1, 2, 3, 7, 8, 10]

print(binary_search(test_list, 0))
print('/n')
print(binary_search(test_list, 1))
print('/n')
print(binary_search(test_list, 8))
print('/n')
print(binary_search(test_list, 10))
print('/n')
print(binary_search(test_list, 9))

