# Problem Set 11.3 - Stacks, Queues, and Deques

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
1. What is a stack? (_Be sure to use the term **LIFO** in your response._)
Answer: A stack is an ordered collection of items where items are added to and removed the end called the "top". **Last in First Out ** is a method of processing the data in which the last items entered are the first to be removed. You can imagine a stack of pancakes stacked on top of each other.

2. What is a queue? (_Be sure to use the term **FIFO** in your response._)
Answer: A queue is an ordered collection of items where the addition of new items happens at one end, called the "rear", and the removal of existing items occurs at the other end, commonly called the "front". ** First In First Out** is a method of processing the data in which the first item entered the queue is the first to be to removed. You can imagine a lunch line, first come first serve.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. Implement a Stack.

2. Implement a Queue.

3. Implement a Deque.


**Use Stacks, Deques, and/or Queue to solve the following three problems in linear runtime.**

4. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

5. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome.

6. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits.
