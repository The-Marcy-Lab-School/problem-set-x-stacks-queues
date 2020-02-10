# Problem Set 11.3 - Stacks, Queues, and Deques

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
1. What is a stack? (_Be sure to use the term **LIFO** in your response._)

    A stack is a data structure that follows the LIFO principle. This essentially means you deal with the most recent items added to the stack
    as a means of insertion or deletion. You can think of it like a adding and removing people from a line at the movies.
    
2. What is a queue? (_Be sure to use the term **FIFO** in your response._)

    A queue is a data structure that follows the FIFO principle. This means that the addition of new elements is added to the end of collections of data,
    while removing elements would happen from the other end, at the front.
    
### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. Implement a Stack.

2. Implement a Queue.

3. Implement a Deque.


**Use Stacks, Deques, and/or Queue to solve the following three problems in linear runtime.**

4. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

5. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome.

6. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits.
