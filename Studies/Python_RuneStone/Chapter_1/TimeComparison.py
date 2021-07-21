#Comparison of times between dictionary and list access
#%%
import timeit

def find_number_in_list(lst, num):
    if num in lst:
        return True
    else:
        return False

short_list = list(range(100))
long_list = list(range(10000000))

#(%) is a Jupyter Magic
%timeit find_number_in_list(short_list, 99)
%timeit find_number_in_list(long_list,9999999)

#slist_time = timeit.timeit(lambda: find_number_in_list(short_list, 99))
#llist_time = timeit.timeit(lambda: find_number_in_list(long_list, 9999999))

short_dict = {x: x*5 for x in range(100)}
long_dict = {x: x*5 for x in range(10000000)}

#sdict_time = timeit.timeit(find_number_in_list(short_dict, 99))
#ldict_time = timeit.timeit(find_number_in_list(long_dict, 9999999))

#print(f"Lookup time change from large to short of list {llist_time/slist_time}.")
#print(f"Lookup time change from large to short of dict {ldict_time/sdict_time}.")

# import time

# d = {'john': 1, 'tim': 2}

# start_time = time.time()
# d['john']
# end_time = time.time()

# print("Time to access dict[0]:", end_time-start_time)

# c = ['john', 'tim']
# start_time = time.time()
# c[0]
# end_time = time.time()

# print("Time to access list[0]:", end_time-start_time)


# %%
