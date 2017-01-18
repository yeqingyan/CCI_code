""" Question 2.4 """
from LinkedList import *


def partition_link_list(head, x):
    """ Partition a linked list around a value x """
    # set up left link list and right link list
    if not head:
        return head
    # dummy node
    left_head, right_head = LinkedList.ListNode(0), LinkedList.ListNode(0)
    left_node, right_node = left_head, right_head
    node = head
    while node:
        if node.val < x:
            left_node.next = node
            left_node = node
        else:
            right_node.next = node
            right_node = node
        node = node.next

    left_node.next = right_head.next
    return left_head.next

link_list = LinkedList.create_random_linklist(1, 10, 20)
link_list.print()
link_list = LinkedList(partition_link_list(link_list.head, 2))
link_list.print()


