import sys
import random


class LinkedList(object):
    # Link list
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self, head):
        self.head = head

    @staticmethod
    def create_random_linklist(min_value, max_value, size):
        i = random.randint(min_value, max_value)
        head = LinkedList.ListNode(i)
        node = head
        for _ in range(size):
            i = random.randint(min_value, max_value)
            node.next = LinkedList.ListNode(i)
            node = node.next
        return LinkedList(head)

    @staticmethod
    def list_to_link_list(vals):
        head = LinkedList.ListNode(0)
        node = head
        for val in vals:
            node.next = LinkedList.ListNode(val)
            node = node.next
        return LinkedList(head.next)

    def print(self):
        node = self.head
        while node:
            sys.stdout.write(str(node.val))
            node = node.next
            if node:
                sys.stdout.write("->")
        sys.stdout.write("\n")

    def have_duplicated(self):
        vals = set()
        node = self.head
        while node:
            if node.val in vals:
                return True
            else:
                vals.add(node.val)
            node = node.next
        return False


    def get_node_value(self, k):
        n = 0
        node = self.head
        while node and n != k:
            node = node.next
            n += 1
        return node.val


    def get_node(self, k):
        n = 0
        node = self.head
        while node and n != k:
            node = node.next
            n += 1
        return node

    @staticmethod
    def compare_linked_list_with_list(head, vals):
        for val in vals:
            if not head:
                return False
            if val != head.val:
                return False
            head = head.next
        return head is None

    def append(self, link_node):
        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = link_node


def append_link_list(linked_list, new_node):
    if not linked_list:
        return new_node
    while linked_list.next:
        linked_list = linked_list.next
    linked_list.next = new_node
