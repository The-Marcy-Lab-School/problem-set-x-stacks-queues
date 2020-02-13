# Question 1
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
        
    def size(self):
        return len(self.items)
        

# Question 2
class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)


# Question 3
class Deque:
    def __init__(self):
        self.items = []
        
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
    if len(string) % 2 != 0:
        return False
        
    opening = set('(')
    matches = set(['(', ')'])
    
    stack = Stack()
    
    for char in string:
        if char in opening:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()
            
    return stack.size() == 0

# Question 5
def is_palindrome(word):
    stack = Stack()
    reversed_word = ""
    for letter in word:
        stack.push(letter)
    
    while not stack.is_empty():
        reversed_word += stack.pop()
        
    return word == reversed_word;
    

# Question 6
def decimal_to_binary(decimalNumber):
    remainderStack = Stack() #stack for 0s and 1s
    
    while decimalNumber > 0:
        remainder = decimalNumber % 2  #first remainder computed is the last digit of the sequence FILO 
        remainderStack.push(remainder)
        decimalNumber = decimalNumber // 2
        
    #Binary string construction
    binaryString = ""
    while not remainderStack.is_empty():
        binaryString = binaryString + str(remainderStack.pop())
    
    return binaryString
        
        
