""" Question 3.2  """


class Stack(object):
    class StackNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.top = None
        # another stack for min value
        self.min = None

    def push(self, item):
        new_node = Stack.StackNode(item)
        new_node.next = self.top
        self.top = new_node

        # min node
        if self.min and self.min < item:
            new_min_node = Stack.StackNode(self.min.val)
        else:
            new_min_node = Stack.StackNode(item)
        new_min_node.next = self.min
        self.min = new_min_node

    def pop(self):
        if self.isEmpty():
            return None
        pop_node = self.top
        self.top = self.top.next
        self.min = self.min.next
        return pop_node.val

    def min(self):
        return self.min.val

    def peek():
        return self.top.val

    def isEmpty():
        return not self.top
