class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f"Node: {self.data}")

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

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

# Question 2
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue2:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0
        
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
            raise IndexError('Cannot Dequeue from an empty queue object')
        
        current = self.front
        self.front = self.front.next
        self.count -= 1
        return current.data

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

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
def is_balanced_parentheses(string):

    start = ['{', '[', '(']
    end = ['}', ']', ')']
    stack = Stack()

    for symbol in string:
        if symbol in start:
            stack.push(symbol)
        elif symbol in end:
            position = end.index(symbol)
            if (stack.size() > 0) and (start[position] == stack.peek()):
                stack.pop()
            else:
                return False

    if stack.size() == 0:
        return True
    else:
        return False

# Question 5
def is_palindrome(string):
    reverse = ''
    stack = Stack()

    for letter in string:
        stack.push(letter)
    for _ in string:
        reverse += stack.pop()

    return reverse == string


# Question 6
def decimal_to_binary(num):
    result = ''
    if num > 1:
        result += decimal_to_binary(num // 2)
    result += f'{num % 2}'
    return result
