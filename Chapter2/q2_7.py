""" Question 2.7 """
from LinkedList import *


def intersection(a, b):
    """  Determine if two linked list intersect， return the intersecting node """
    a_nodes = []
    while a:
        a_nodes.append(a)
        a = a.next

    while b:
        if b in a_nodes:
            return b
        b = b.next

    return None

a = LinkedList.list_to_link_list([1, 2, 3, 4, 5, 6, 7])
b = a.get_node(5)
assert intersection(a.head, b) == b


