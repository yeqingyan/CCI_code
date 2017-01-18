""" Question 2.1 """
from LinkedList import *


def remove_dups(head):
    """ remove duplicates from an unsorted linked list """
    if not head:
        return
    values = set({head.val})
    pre = head
    n = head.next
    while n:
        if n.val in values:
            pre.next = n.next
        else:
            values.add(n.val)
            pre = n
        n = n.next


def remove_dups_no_buf(head):
    """ remove duplicates from an unsorted linked list without use any temporary buffer """
    cur_node = head
    while cur_node:
        pre = cur_node
        next_node = cur_node.next
        while next_node:
            if next_node.val == cur_node.val:
                # Remove it
                pre.next = next_node.next
                next_node = next_node.next
            else:
                pre = next_node
                next_node = next_node.next
        cur_node = cur_node.next

link_list = LinkedList.create_random_linklist(1, 5, 10)
remove_dups(link_list.head)
assert not link_list.have_duplicated()
link_list = LinkedList.create_random_linklist(1, 5, 10)
remove_dups_no_buf(link_list.head)
assert not link_list.have_duplicated()
