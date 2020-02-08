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
        
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        
    def is_empty(self):
        return self.top is None
        
    def pop(self):
        if self.is_empty():
            raise IndexError('This stack is empty.')
        current = self.top
        self.top = current.next
        self.count -= 1
        return current.data
        
    def peek(self):
        return self.top.data
        
    def size(self):
        return self.count
    
# Question 2
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0
        
    def is_empty(self):
        return self.count == 0
        
    def enqueue(self,data):
        if self.is_empty():
            self.front = Node(data)
            self.back = Node(data)
        else:
            current = self.back
            self.back = Node(data)
            current.next = self.back
        self.count += 1
        return self.count
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty Queue')
        current = self.front
        self.front = self.front.next
        self.count -= 1
        return current.data
        
    def size(self):
        return self.count
        

# Question 3
class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0
    
    def size(self):
        return self.count
        
    def is_empty(self):
        return self.count == 0
    
    def add_front(self,data):
        if self.is_empty():
            self.front = Node(data)
            self.back = Node(data)
        else:
            current = self.front
            self.front = Node(data)
            current.next = self.front
        self.count += 1
        return self.count
    
    def add_rear(self,data):
        if self.is_empty():
            self.front = Node(data)
            self.back = Node(data)
        else:
            current = self.back
            self.back = Node(data)
            current.next = self.back
        self.count += 1
        return self.count
        
    def remove_front(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty Queue')
        current = self.front
        self.front = self.front.next
        self.count -= 1
        return current.data
  
  
    def remove_rear(self):
        if self.is_empty():
            raise IndexError('Cannot dequeue from an empty Queue')
        current = self.back
        self.back = self.back.next
        self.count -= 1
        return current.data

# Question 4
def is_balanced_parentheses(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.is_empty():
            return True
    return False
    
        
# Question 5
def is_palindrome(string):
    stack = Stack()
    new_string = ""
    for letter in string:
        stack.push(letter)
    for letter in string:
        new_string += stack.pop()
    return new_string == string

# Question 6
def decimal_to_binary(dec_num):
    stack = Stack()
    while dec_num > 0:
        num = dec_num  % 2
        stack.push(num)
        dec_num = dec_num // 2
    
    new_string = ""
    while not stack.is_empty():
        new_string += str(stack.pop())
    return new_string