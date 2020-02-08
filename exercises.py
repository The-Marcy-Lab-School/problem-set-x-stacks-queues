class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
# Question 1
class Stack:
    def __init__(self,data=None):
        self.head = Node(data)
        self.length = 0
        
    def push(self, new):
        newNode = Node(new)
        hold = self.head
        self.head = newNode
        newNode.next = hold
        self.length += 1
        
    def pop(self):
        hold = self.head
        self.head = self.head.next
        self.length -= 1
        return hold.data
        
    def is_empty(self):
        return self.head.next == None
        
    def size(self):
        return self.length
    
    def peek(self):
        return self.head.data

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
        
    def size(self):
        return self.count

# Question 4
def is_balanced_parentheses(symbol_string):
    holder = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '({[':
            holder.push(symbol)
        else:
            if holder.is_empty():
                balanced = False
            else: 
                holder.pop()
        index += 1
    if balanced and holder.is_empty():
        return True 
    return False


# Question 5
def is_palindrome(string):
    new_stack = Stack()
    reverse_string = ''
    for i in range(len(string)):
        new_stack.push(string[i])
    for i in range(len(string)):
        reverse_string += new_stack.pop()
    
    return string == reverse_string
    

# Question 6
def decimal_to_binary(number):
    new_stack = Stack()
    binary_string = ''
    while number > 0:
        new_stack.push(number % 2)
        number = number // 2
    while not new_stack.is_empty():
        binary_string += str(new_stack.pop())
    
    return binary_string