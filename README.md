# Problem Set: Stacks and Queues

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

Complete code challenges in `exercises.js`. 

Use Test Driven Development to guide you. For JavaScript, run `npm install` to download dependencies. Run `npm test` to run tests locally. Ensure all tests are passing before submitting this problem set.

## Short Response Questions

#### 1. What is a stack? What are the essential operations for a stack? (_Be sure to use the term **LIFO** in your response._)

#### 2. What is a queue? What are the essential operations for a queue? (_Be sure to use the term **FIFO** in your response._)

## Class Coding Exercises

#### 1. Implement a Stack.

#### 2. Implement a Queue.

## Interview Problems 

**Use a Stack to solve the following three problems in linear runtime.** 

These are common interview problems and you can find an algorithm to solve them online. We encourage you to **spend at least 15 minutes** attempting to come up with an algorithm on your own before looking it up. If you find an algorithm online, **STOP before copying** and take time to **internalize the algorithm**.

> Note: You should ideally be using the `Stack` class you just implemented. If your `Stack` class is not working properly, you may use a normal array, but limit yourself to stack-like operations (`push`, `pop`, peeking at the last element). Upon review, you will likely be asked to resubmit with a functional `Stack` class.

#### 3. Write a function, `is_balanced_parentheses`, that returns a boolean value based on whether a string has balanced parentheses. Parentheses are balanced if: **(1)** Every open parenthesis has a corresponding closing parenthesis and **(2)** every pair of parentheses begins with an opening parenthesis.

  Examples:
  ```
  ()()    => balanced
  ((()))  => balanced
  )()(    => unbalanced
  (()))   => unbalanced
  ```

#### 4. Write a function, `is_palindrome`, that takes a string input and determines if the input is a palindrome (the input is identical in reverse).

  Examples:
  ```
  'abcba'   => palindrome
  'abcde'   => not a palindrome
  '12321'   => palindrome
  '12345'   => not a palindrome
  ```

#### 5. Write a function, `decimal_to_binary`, that takes an integer input and returns its binary representation as a string of digits. Do not use any methods that convert numbers to binary (such as `num.toString(2)`)

  Examples:
  ```
  0   => 0
  1   => 1
  2   => 10
  3   => 11
  4   => 100
  5   => 101
  6   => 110
  7   => 111
  8   => 1000
  ```
