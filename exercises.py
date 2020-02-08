# Question 1
class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        return self.data.append(el)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.data == []

# Question 2
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, el):
        return self.data.append(el)

    def dequeue(self):
        return self.data.pop(0)

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.data == []


# Question 3
class Deque:
    """
    Implements a custom Deque class
    add_front, add_rear, remove_front, remove_rear, is_empty, size
    """
    def __init__(self):
        self.data = []

    def add_front(self, el):
        return self.data.insert(0, el)

    def add_rear(self, el):
        return self.data.append(el)

    def remove_front(self):
        return self.data.pop(0)

    def remove_rear(self):
        return self.data.pop()

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.data == []

# Question 4
def is_balanced_parentheses(s: str) -> bool:
    if s[0] == ')': return False
    stack = Stack()
    for char in s:
        if char == '(':
            stack.push(char)
        else:
            stack.pop()
    return stack.size() == 0

# Question 5
def is_palindrome(s: str) -> bool:
    stack = Stack()
    for char in s:
        stack.push(char)
    rev_s = ""
    for _ in range(len(s)):
        rev_s += stack.pop()
    return s == rev_s

# Question 6
def decimal_to_binary(n: int) -> str:
    stack = Stack()
    while n > 0:
        stack.push(n % 2)
        n = n // 2
    bin_s = ""
    for _ in range(stack.size()):
        bin_s += str(stack.pop())
    return bin_s
