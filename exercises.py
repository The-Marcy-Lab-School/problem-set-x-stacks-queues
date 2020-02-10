# Question 1
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)
        

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
    
    def is_empty(self):
        return self.top is None
        
    def pop(self):
        if self.is_empty():
            raise IndexError('This stack is empty')
        current = self.top
        self.top = current.next
        self.count -= 1
        return current.data
        
    
    def peek(self):
        return self.top.data
        
    def size(self):
        return self.count
        

# stack = Stack()
# stack.push('a')
# stack.push('b')
# stack.push('c')
# print(stack.pop())
# print(stack.size)

# Question 2
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def enqueue(self, items):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
        


# Question 3
class Deque:
    """Implements a custom Deque class"""
    def __init__(self):
        self.items =[]
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self, item):
        self.items.append(item)
    
    def add_rear(self, item):
        self.items.insert(0, item)
        
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
        

# Question 4
def is_balanced_parentheses(string):
    stack = Stack()
    balanced = True
    index = 0
    
    while index < len(string) and balanced:
        par = string[index]
        if par == '(':
            stack.push(par)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
                
        index += 1
        
    if balanced and stack.is_empty():
        return True
    else:
        return False
                    
# print(is_balanced_parentheses('()()') == True)

# Question 5
def is_palindrome(string):
    stack = Stack()
    reversed_word = ""
    

# print(is_palindrome('ovo'))

# Question 6
def decimal_to_binary(decimal):
    rem_stack = Stack()
    binary = ""
    
    while decimal > 0:
        rem = decimal % 2
        rem_stack.push(rem)
        decimal = decimal // 2
    
    while not rem_stack.is_empty():
        binary = binary + str(rem_stack.pop())
        
    return binary

# print(decimal_to_binary(7))
# print(decimal_to_binary(42))

