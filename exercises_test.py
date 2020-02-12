from exercises import *
import pytest

#@pytest.mark.skip(reason="Delete this once you've implemented the Stack class")
def test_stack():
    stack = Stack()
    assert stack.is_empty()
    stack.push('a')
    assert not stack.is_empty()
    assert stack.pop() == 'a'
    assert stack.is_empty()
    stack.push('b')
    stack.push('c')
    assert stack.peek() == 'c'
    assert stack.size() == 2
    assert stack.pop() == 'c'

# @pytest.mark.skip(reason="Delete this once you've implemented the Queue class")
def test_queue():
    queue = Queue()
    assert queue.is_empty()
    queue.enqueue('1st')
    assert not queue.is_empty()
    queue.enqueue('2nd')
    queue.enqueue('3rd')
    assert queue.size() == 3
    assert queue.dequeue() == '1st'
    assert queue.size() == 2

# @pytest.mark.skip(reason="Delete this once you've implemented the Deque class")
def test_deque():
    deque = Deque()
    assert deque.is_empty()
    deque.add_rear(4)
    deque.add_rear('Dog')
    deque.add_front('Cat')
    deque.add_front(True)
    assert deque.size() == 4
    assert not deque.is_empty()
    deque.add_rear(8.4)
    assert deque.remove_rear() == 8.4
    assert deque.remove_front() == True

# @pytest.mark.skip(reason="Delete this once implemented")
def test_is_balanced_parentheses():
    assert is_balanced_parentheses('()()') == True
    assert is_balanced_parentheses('()((') == False
    assert is_balanced_parentheses('((()))()') == True
    assert is_balanced_parentheses(')()(') == False

# @pytest.mark.skip(reason="Delete this once implemented")
def test_is_palindrome():
    assert is_palindrome('abba')
    assert is_palindrome('racecar')
    assert not is_palindrome('palindrome')
    assert not is_palindrome('08052020')
    assert is_palindrome('02022020')

# @pytest.mark.skip(reason="Delete this once implemented")
def test_decimal_to_binary():
    assert decimal_to_binary(7) == '111'
    assert decimal_to_binary(42) == '101010'
    assert decimal_to_binary(225) == '11100001'
