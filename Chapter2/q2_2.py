""" Question 2.2 """
from LinkedList import *


def kth_to_last(head, k):
    """ find the kth to last element of a single linked list """
    if not head:
        return -1
    size = 1
    node = head
    while node.next:
        node = node.next
        size += 1
    i = size - k - 1
    node = head
    while i != 0:
        node = node.next
        i -= 1
    return node.val


link_list = LinkedList.create_random_linklist(1, 100, 20)
i = link_list.get_node_value(11)
link_list.print()
assert kth_to_last(link_list.head, 9) == i


