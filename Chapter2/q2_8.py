""" Question  2.8 """
from LinkedList import *


def loop_detection(looped_list):
    """  Returns the node at the begining of the loop """
    if not looped_list.next or not looped_list.next.next:
        return None
    slow = looped_list.next
    fast = looped_list.next.next
    while slow and fast and slow != fast:
        slow = slow.next
        fast = fast.next.next

    if not slow or not fast:
        return None
    # meet
    loop_start = looped_list
    while loop_start != slow:
        loop_start = loop_start.next
        slow = slow.next
    return loop_start

a = LinkedList.list_to_link_list([1, 2, 3, 4, 5])
loop_start = a.get_node(2)
a.append(loop_start)
assert loop_detection(a.head) == loop_start
