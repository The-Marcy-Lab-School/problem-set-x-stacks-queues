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


# ourStack = Stack()
# ourStack.push('a')
# ourStack.push('b')
# ourStack.push('c')
# print(ourStack.pop())
# print(ourStack.size())

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
def is_balanced_parentheses(string):
    tempStack = Stack()
    balanced = True
    i = 0
    while i < len(string) and balanced:
        curl = string[i]
        if curl in '({[':
            tempStack.push(curl)
        else:
            if tempStack.is_empty():
                balanced = False
            else: 
                tempStack.pop()
        i += 1
    if balanced and tempStack.is_empty():
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
def decimal_to_binary(decimal):
    
    tempStack = Stack()
    while decimal > 0:
        tempStack.push(decimal % 2)
        decimal = decimal // 2
        
        string = ""
        while not tempStack.is_empty():
            string += str(tempStack.pop())
        return string