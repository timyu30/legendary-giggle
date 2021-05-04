#Infix to Postfix of expressions implemented with a stack
#and dictionary
#%%
class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, num):
        self.list.append(num)
    
    def pop(self):
        return self.list.pop()
    
    def is_Empty(self):
        return len(self.list) == 0
    
    def peek(self):
        if len(self.list) > 0:
            return self.list[len(self.list)-1]
        else: 
            return None

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_Empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_Empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infix_to_postfix("( A + B ) * ( C + D )"))
print(infix_to_postfix("( A + B ) * C"))
# %%
lists = []
#error out of range
#print(lists[0])
# %%
