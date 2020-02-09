# Question 1
class Node: #For the Stack class
    def __init__(self, data = None):
        self.next = None
        self.data = data

    def __repr__(self):
        return str(self.data)


# class Stack:
#     def __init__(self):
#         self.top = None
#         self.count = 0

#     def is_empty(self):
#         return self.top is None

#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
#         self.count += 1

#     def pop(self):
#         if self.is_empty():
#             raise IndexError('Stack is empty.')
#         current = self.top
#         self.top = current.next
#         self.count -= 1
#         return current.data

#     def peek(self):
#         return self.top.data

#     def size(self):
#         return self.count

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Question 2
class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.count = 0

    def is_empty(self):
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
            raise IndexError('Queue is empty.')
        else:
            current = self.front
            self.front = self.front.next
        self.count -= 1
        return current.data

    def size(self):
        return self.count

# Question 3
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

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
    starting = ['{', '[', '(']
    ending = ['}', ']', ')']

    for sym in string:
        if sym in starting:
            stack.push(sym)
        elif sym in ending:
            position = ending.index(sym)
            if (stack.size() > 0) and (starting[position] == stack.peek()):
                stack.pop()
            else:
                return False

    if stack.size() == 0:
        return True

print(is_balanced_parentheses('()'))

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


