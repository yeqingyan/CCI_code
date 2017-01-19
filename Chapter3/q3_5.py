""" Question 3.5  """
from Stack import *
import random


def sort_stack(stack):
    temp_stack = Stack()
    max_value = stack.pop()
    stack_size = 0
    while not stack.isEmpty():
        value = stack.pop()
        if value > max_value:
            max_value, value = value, max_value
        temp_stack.push(value)
        stack_size += 1
    stack.push(max_value)

    max_value = None
    second_max_value = None
    while stack_size != 0:
        max_value = temp_stack.pop()
        stack_size -= 1
        for _ in range(stack_size):
            value = temp_stack.pop()
            if value > max_value:
                max_value, value = value, max_value
            stack.push(value)

        if stack_size == 0:
            second_max_value = None
            break
        second_max_value = stack.pop()
        stack_size -= 1
        for _ in range(stack_size):
            value = stack.pop()
            if value > second_max_value:
                second_max_value, value = value, second_max_value
            temp_stack.push(value)
        stack.push(max_value)
        stack.push(second_max_value)
        max_value = None
    if max_value:
        stack.push(max_value)

s = Stack()
for _ in range(4):
    s.push(random.randint(1, 100))
Stack.print_stack(s)
sort_stack(s)
print("After sort:")
Stack.print_stack(s)
