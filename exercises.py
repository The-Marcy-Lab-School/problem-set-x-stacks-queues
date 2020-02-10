class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)

# Question 1
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1 #stack gets larger
        
    def is_empty(self):
        return self.top is None
            
    def pop(self):
        if self.is_empty():
            raise IndexError("This stack is empty")
        current = self.top
        self.top = current.next
        return current.data
        # local to the scope, current grarbage collected each time.
        self.count -= 1
        
    def peek(self):
        return self.top.data
        # You could use -1 as an index to get the last item on the item
        # return self.items[-1]
        
    def size(self):
        return self.count


ourStack = Stack()
ourStack.push('a')
ourStack.push('b')
ourStack.push('c')
print(ourStack.pop())
print(ourStack.size())

# Question 2
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0

    def is_empty(self,data):
        return self.count == 0
        
    def enqueue(self, data):
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
            raise IndexError("Cannot dequeue from an empty queue")
        current = self.front
        self.front = self.front.next
        self.count -= 1
        return current.data
    
    def size(self):
        return self.count
        
# Question 3
class Deque:
    def __init__(self):
            self.data = []

    def add_front(self, data):
        return self.data.insert(0, data) # Use insert to get around

    def add_rear(self, data):
        return self.data.append(data)

    def remove_front(self):
        return self.data.pop(0)

    def remove_rear(self):
        return self.data.pop()

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.data == []

# Question 4
def is_balanced_parentheses():
    
    # starting = set('([{')
    # matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    # stack = []
    # P
    # This function will take in a string that contains a number of brackets, it that checks that each openning bracket or parenthesis has it's own closings tag. Thus being balanced. As all things should be...
    # E print(is_balanced_parentheses("[('(', ')'))")
    #   print(is_balanced_parentheses("[(', (', ')'))")
    #   print(is_balanced_parentheses("[(', ')]"))
    # D dictionaries and strings
    # A
    # Create dictionary to record brackets count
    # loop through string and record each instance of a type of bracket.
    # loop through dictionary and check if every entry/property is is even. (entry % 2 == 1)
    # If any entry is odd then return "false".
    # Note this algorithm doesnt check if they are in the right order like a coding IDE. 


def check_is_balanced_parentheses(data)
    tempStack = Stack()
    i = 0 #Index Control
    b = true
    while i < len(data) and b:
        if curl = data[i]

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
def is_palindrome(ourString):
    tempStack = Stack()
    reversedWord = ""
    
    for char in ourString:
        tempStack.push(char)
    
    while not tempStack.is_empty():
        reversedWord += tempStack.pop()
    
    return ourString == reversedWord

# Question 6
def decimal_to_binary():
    pass
