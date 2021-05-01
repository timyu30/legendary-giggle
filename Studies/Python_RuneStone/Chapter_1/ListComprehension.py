hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices: total_price += price

average_price = total_price/len(prices)
print(f"Average Haircut Price: {average_price}")

new_prices = [price-5 for price in prices]
print(new_prices)

total_revenue = 0
for day in range(len(last_week)):
  total_revenue += (last_week[day] * prices[day])
print(f"Total Revenue: {total_revenue}")
average_daily_revenue = total_revenue/7


#selecting hairstyles under 30 from new_prices while using common index in list comprehension
cuts_under_30 = [hairstyles[day] for day in range(len(new_prices)) if new_prices[day]< 30]

print(cuts_under_30)

cu30 = []

for day in range(len(new_prices)):
    if new_prices[day] < 30:
        cu30.append(hairstyles[day])

print(cu30)

#%%
def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

for element in [1,[1,2],(1,2), {'1':2}, "This is a string", 1.2]: 
    print(element, " is iterable : ", iterable(element))
# %%
iterator_obj = iter("String")
print(type(iterator_obj))
for element in iterator_obj:
    
    print(element, next(iterator_obj),end = " ")
#print(next(iterator_obj))

# iterable is an object that can be iterated over, for example
# strings, dict, lists, tuples, custom obj
# when iterable is passed to iter() a iterator object is created
# the iterator obj has a __next__() method, which returns the next
# #item in the object  

#%%

#using __next__() method insead of next() function to iterate the iterable with iterator
list_age = list(range(10))

iter_obj = iter(list_age)
#iter_obj = list_age.__iter__()
while True:
    try:
        print(iter_obj.__next__())
    except:
        print("\n Throwing 'StopIterationError' I cannot count more.")
        break
# %%
class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num -1
if __name__ == '__main__' :
    a,b = 2,5
    c1 = Counter(a,b)
    c2 = Counter(a,b)

# no iter() or next()
    for i in c1:
        print ("Eatting pizza from for loop " + str(i))

# use iter()

    #iterators only pass through ONCE!!! while loop would return False immediately 
    #if testing iterator obj c1 again
    #iterator_obj = iter(c1)
    iterator_obj = iter(c2)
    try:
        while True:
            print("Eatting pizza from while loop", (next(iterator_obj)))
    except:
        print("Too much food, End of iterator")
# %%
x,y = (1,3)
print('x is ' + str(x), y)
# %%
print(not bool([]), bool(0))

# %%
class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)

def rev_String(name = "Timothy"):
    s = Stack()
    for i in name:
        s.push(i)

    #print(s.peek())

    a = ''
    #print(s.is_empty())
    while not s.is_empty():
        a += (s.pop())

    print(a)
    return a
# %%
def par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()


print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False