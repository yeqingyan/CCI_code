""" Question 2.6 """
from LinkedList import *


def palindrome(head):
    """ Check a linked list is a palindrome """
    nodes = []
    while head:
        nodes.append(head.val)
        head = head.next

    if len(nodes) % 2 == 0:
        left = int(len(nodes) / 2 - 1)
        right = int(len(nodes) / 2)
    else:
        left = int((len(nodes) / 2) - 1)
        right = int((len(nodes) / 2) + 1)
    while left >= 0:
        if nodes[left] != nodes[right]:
            return False
        left -= 1
        right += 1
    return True

a = LinkedList.list_to_link_list([1, 2, 3, 4, 5, 6, 7])
assert not palindrome(a.head)
b = LinkedList.list_to_link_list([1, 2, 3, 4, 3, 2, 1])
assert palindrome(b.head)
c = LinkedList.list_to_link_list([1, 2, 3, 4, 5, 6])
assert not palindrome(c.head)
d = LinkedList.list_to_link_list([1, 2, 3, 3, 2, 1])
assert palindrome(d.head)
