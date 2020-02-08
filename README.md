# Problem Set 11.3 - Stacks, Queues, and Deques

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
1. What is a stack? (_Be sure to use the term **LIFO** in your response._)

    A stack is an abstract data structure with a last in first out design. Essentially the first thing you add to a stack can only be accessed after you've moved past everything that was added after it. Items added are always removed in reverse order of its entry.

2. What is a queue? (_Be sure to use the term **FIFO** in your response._)

    A queue is an abstract data structure with a first in first out design. It's more like a tunnel than anything, you can only add to the back and only remove from the front. Items added are always removed in the same order of its entry.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. Implement a Stack.

2. Implement a Queue.

3. Implement a Deque.


**Use Stacks, Deques, and/or Queue to solve the following three problems in linear runtime.**

4. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

5. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome.

6. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits.
