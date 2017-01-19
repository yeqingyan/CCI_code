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
        self.num_stacks = 0

    def push(self, item):
        new_node = StackOfPlates.StackNode(item)
        # new stack
        if not self.top_nodes:
            self.top_nodes = StackOfPlates.TopNode(new_node)
            self.current_threshold += 1
            self.num_stacks += 1
        else:
            if self.current_threshold >= self.THRESHOLD:    # push to a full stack
                new_top_node = StackOfPlates.TopNode(new_node)
                new_top_node.next = self.top_nodes
                self.top_nodes = new_top_node
                self.current_threshold = 1
                self.num_stacks += 1
            else:   # normal push
                new_node.next = self.top_nodes.node
                self.top_nodes.node = new_node
                self.current_threshold += 1
        # print("threshold {} stacks {}".format(self.current_threshold, self.num_stacks))

    def pop(self):
        if not self.top_nodes:
            return None
        pop_node = None
        if self.top_nodes.node.next == None:    # pop the last node in Stack
            pop_node = self.top_nodes.node
            self.top_nodes = self.top_nodes.next
            self.current_threshold = self.THRESHOLD
            self.num_stacks -= 1
        else:   # normal pop
            pop_node = self.top_nodes.node
            self.top_nodes.node = self.top_nodes.node.next
            self.current_threshold -= 1
        return pop_node.val

    def peek(self):
        return self.top_nodes.node.val

    def isEmpty(self):
        return not self.top_nodes

    def popAt(self, index):
        temp_stack = []
        size = self.current_threshold + self.THRESHOLD * (self.num_stacks-1)
        pop_times = size - index
        if pop_times < 0:
            return None

        i = 0
        while i != pop_times: 
            temp_stack.append(self.pop())
            i += 1
        return_node = temp_stack.pop()
        while temp_stack:
            self.push(temp_stack.pop())
        return return_node


import random 
a = StackOfPlates(2)
for _ in range(10):
    a.push(random.randint(1, 100))
    print(a.peek())

print("Pop index 4: {}".format(a.popAt(4)))
for _ in range(9):
    print(a.pop())
