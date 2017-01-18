""" Question 3.3  """


class StackOfPlates(object):
    class StackNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    class TopNode(object):
        def __init__(self, top_node):
            self.node = top_node
            self.next = None

    def __init__(self, threshold):
        self.THRESHOLD = threshold
        self.current_threshold = 0
        self.top_nodes = None

    def push(self, item):
        new_node = StackOfPlates.StackNode(item)
        # new stack
        if not self.top_nodes:
            self.top_nodes = StackOfPlates.TopNode(new_node)
            self.current_threshold += 1
        else: 
            if self.current_threshold >= self.THRESHOLD:    # push to a full stack
                new_top_node = StackOfPlates.TopNode(new_node)
                new_top_node.next = self.top_nodes
                self.top_nodes = new_top_node
                self.current_threshold = 0
            else:   # normal push
                new_node.next = self.top_nodes.node
                self.top_nodes.node = new_node
                self.current_threshold += 1

    def pop(self):
        if not self.top_nodes:
            return None
        pop_node = None
        if self.top_nodes.node.next == None:    # pop the last node in Stack
            pop_node = self.top_nodes.node
            self.top_nodes = self.top_nodes.next
            self.current_threshold = self.THRESHOLD
        else:   # normal pop
            pop_node = self.top_nodes.node
            self.top_nodes.node = self.top_nodes.node.next
            self.current_threshold -= 1
        return pop_node.val

    def peek(self):
        return self.top_nodes.node.val

    def isEmpty():
        return not self.top_nodes

import random 
a = StackOfPlates(2)
for _ in range(10):
    a.push(random.randint(1, 100))
    print(a.peek())

for _ in range(10):
    print(a.pop())
