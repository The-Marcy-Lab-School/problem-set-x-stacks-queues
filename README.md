# Problem Set 11.3 - Stacks, Queues, and Deques

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
1. What is a stack? (_Be sure to use the term **LIFO** in your response._)

- A stack is an ordered collection of items. You can add and remove items on this stack, but in the order that they came from. When you add to a stack, you add it to the top, so the recent items added are at the top, while the older items are near the base of the stack. When you remove an item, you start removing from the top. This process is referred to as LIFO, which stands for 'Last In, First Out'. It's the last item to be added, and the first item to be removed, due to the ordered structure of the stack.

2. What is a queue? (_Be sure to use the term **FIFO** in your response._)

- A queue is an ordered collection of items. When you add an item to a queue, it is added at the "rear" of the collection, however you would like to call it. When items are removed, however, they are removed from the "front" of the queue. It's like being in line at an amusement park, waiting to get one a ride. You're the first person there, and others will line up behind you - that's how you add items to a queue. When the ride is available, you're the first person to be able to get on the ride, and the people behind you will also join the ride in the order that they were added, which is how you remove items from a queue. This process is referred to as FIFO, which stands for 'First In, First Out'. It's the first item added, and the first item to be removed.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. Implement a Stack.

2. Implement a Queue.

3. Implement a Deque.


**Use Stacks, Deques, and/or Queue to solve the following three problems in linear runtime.**

4. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

5. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome.

6. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits.
