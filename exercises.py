# Question 1

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def is_empty(self):
        return self.items == []
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

# Question 2
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)
    
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

    def size(self):
        return len(self.items) 
    
    def add_front(self,item):
        self.items.append(item)

    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)
# Question 4
def is_balanced_parentheses(string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        
        index += 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False


# Question 5
def is_palindrome(string):
    deque = Deque()
    for letter in string:
        deque.add_rear(letter)
    
    isEqual = True

    while deque.size() > 1 and isEqual:
        firstLetter = deque.remove_front()
        lastLetter = deque.remove_rear()
        if firstLetter != lastLetter:
            isEqual = False
    
    return isEqual

# Question 6
def decimal_to_binary(number):
    s = Stack()

    while number > 0:
        remainder = number % 2
        s.push(remainder)
        number = number // 2

    binary = ''
    while not s.is_empty():
        binary = binary + str(s.pop())

    return binary
