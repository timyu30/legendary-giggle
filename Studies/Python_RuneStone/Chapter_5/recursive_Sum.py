#Recursion is a method of solving problems 

#using for loop to sum numbers
def for_list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum

print(for_list_sum([1,3,5,7,9]))

#using recursion to sum numbers
def recursion_list_sum(num_list):
    the_sum = 0
    #base case
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + recursion_list_sum(num_list[1:])

print(recursion_list_sum([1,3,5,7,9]))