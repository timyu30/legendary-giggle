#Decimal to binary numbers
#Decimal to hexidecimal numbers or any base
class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, num):
        self.list.append(num)
    
    def pop(self):
        return self.list.pop()
    
    def is_Empty(self):
        return len(self.list) == 0


def convert_decimal_to_base(num,base):
    s = Stack()
    #hexbase has alphabets to represent 10-16, string will be used to index the character to store into stack
    hexBase = "0123456789ABCDEF"

    #populate the stack with remainder
    while num > 0:
        remainder = num % base
        s.push(remainder)
        num = num//base

    #reverse stack by pop method
    converted_base = ""
    while not s.is_Empty():
        if base < 9:
            converted_base = converted_base + str(s.pop())
        else:
            converted_base = converted_base + hexBase[s.pop()]
    print(converted_base)
    return converted_base

convert_decimal_to_base(233, 2)
convert_decimal_to_base(26, 16)
