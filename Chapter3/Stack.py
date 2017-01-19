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

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val

    def isEmpty(self):
        return not self.top

    @staticmethod
    def print_stack(stack):
        temp = Stack()
        while not stack.isEmpty():
            val = stack.pop()
            print(val)
            temp.push(val)

        while not temp.isEmpty():
            stack.push(temp.pop())


        