# Question 1
class Stack:
    """Implements a custom Stack class"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
        
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        return self.items[len(self.items) - 1]

# Question 2
class Queue:
    """Implements a custom Queue class"""
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0, item)
     
    def dequeue(self):
        return self.items.pop()
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)

# Question 3
class Deque:
    """Implements a custom Deque class"""
    def __init__(self):
        self.items = []
        
    def add_front(self, item):
        self.items.append(item)
        
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
        
    def remove_rear(self):
        return self.items.pop(0)
        
    def is_empty(self):
        return self.items == []
        
    def size(self):
        return len(self.items)
        
# Question 4
def is_balanced_parentheses(string):
    stack = Stack()
    
    for char in string:
        if char == '(':
            stack.push(char)
        else:
            stack.pop()
            
    if stack.size() == 0:
        return True
    else:
        return False
 
# Question 5
def is_palindrome(string):
    stack = Stack()
    
    revString = ''
    
    for letter in string:
        stack.push(letter)
        
    for letter in string:  #while not stack.is_empty():
        revString += stack.pop()
        
    return string == revString

# Question 6
def decimal_to_binary(num):
    stack = Stack()
    
    while num > 0:
        r = num % 2
        stack.push(r)
        
    binStr = ''
    while stack:
        binStr = binStr + str(stack.pop())
        
    return binStr