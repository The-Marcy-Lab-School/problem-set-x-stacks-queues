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

    def add_front(self, item): #Front is from the right
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

    stack = Stack()

    # starting = set('([{')
    # matches = set([('(', ')'), ('[', ']'), ('{', '}')])
    # stack = []

    for sym in string:
        if sym == '(':
            stack.push(sym)


# Question 5
def is_palindrome(string):
    stack = Stack()
    newStack = []

    for letter in string:
        stack.push(letter)

# Question 6
def decimal_to_binary():
    pass
