""" Question 3.4  """
from Stack import *
import random


class MyQueue(object):
    def __init__(self):
        self.queue_stack = Stack()
        self.temp_stack = Stack()
        self.first = None
    
    def add(self, item):
        self.queue_stack.push(item)
        if self.first == None:
            self.first = item

    def remove(self):
        while not self.queue_stack.isEmpty():
            self.temp_stack.push(self.queue_stack.pop())

        remove_val = self.temp_stack.pop()
        self.first = self.temp_stack.peek()
        while not self.temp_stack.isEmpty():
            self.queue_stack.push(self.temp_stack.pop())
        return remove_val

    def peek(self):
        return self.first

    def isEmpty(self):
        return self.queue_stack.isEmpty()


q = MyQueue()
print("Push")
for _ in range(10):
    add_val = random.randint(1, 100)
    q.add(add_val)
    print(add_val)

print("Pop")
for _ in range(10):
    print(q.remove())