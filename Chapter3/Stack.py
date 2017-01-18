class Stack(object):
    class StackNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Stack.StackNode(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        pop_node = self.top
        self.top = self.top.next
        return pop_node.val

    def peek():
        return self.top.val

    def isEmpty():
        return not self.top
