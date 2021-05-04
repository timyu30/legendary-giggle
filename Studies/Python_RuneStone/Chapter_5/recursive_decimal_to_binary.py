#integer to hex or binary with conversion
class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, num):
        self.items.append(num)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0 
        
    

def to_str(n, base):
    r_stack = Stack()
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


print(to_str(1453, 16))