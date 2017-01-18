class Queue(object):
    class QueueNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        last_node = Queue.QueueNode(item)
        if not self.first:
            self.first = last_node
        else:
            self.last.next = last_node
        self.last = last_node

    def remove(self):
        if self.isEmpty():
            return None
        remove_node = self.first
        self.first = self.first.next
        if not self.first:
            self.last = None
        return remove_node.val

    def peek():
        return self.first.val

    def isEmpty():
        return not self.first
