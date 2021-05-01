#%%
import copy
class Stack:

    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def show(self):
        for i in self.data:
            print(i, end  = "-->")
    
    def pop(self):
        return self.data.pop()
    
    def is_Empty(self):
        return not len(self.data) > 0

        
s = Stack()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
#s.show()
n = (s)
s.add(5)
s.show()
print("\nbetween originals")
n.show()

#function to remove all values in stack
def clear_All(n):
    stack = n
    #print(len(stack.data))
    for i in range(len(stack.data)):
        stack.data.pop()
        #print(i)
        # stack.show()
    
    return stack


#print("Hello")
new_stack = clear_All(s)
print(new_stack.is_Empty())
#new_stack.show()
#s.show()
n.show()
# %%
# old_list = [[1,2], [3,4]]
# new_list = (old_list)

# new_list.append([5,6])
# print(old_list)
# print("Copy:", new_list)