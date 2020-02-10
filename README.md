# Problem Set 11.3 - Stacks, Queues, and Deques

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
1. What is a stack? (_Be sure to use the term **LIFO** in your response._)
    A stack is an ordered collection of items. 
    When you add to a stack, 
    you add it to the top of it like a fresh pancake on a 'stack' of pancakes, the most recent is on the top.
    To  remove an item, you start removing from the top following the LIFO process, 
    which stands for 'Last In, First Out'. It's the last item to be added, 
    and the first item to be removed, due to the ordered structure of the stack.

2. What is a queue? (_Be sure to use the term **FIFO** in your response._)
 
    Like a stack, a queue is a collection of items that is ordered
    Adding an item to a queue,however, puts it to the rear of the collection
    and when an item is removed it is from the front of the queue
    It is essentially a line where items are handled in the order they come in.
    This is the FIFO process, or 'First In, First Out'. It's the first item added, and the first item to be removed.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. Implement a Stack.

2. Implement a Queue.

3. Implement a Deque.


**Use Stacks, Deques, and/or Queue to solve the following three problems in linear runtime.**

4. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

5. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome.

6. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits.
