""" Question 2.5 """
from LinkedList import *


def sum_lists_reversed(a, b):
    """ adds the two number(represent by link list) returns the sum as linked list """
    sum_result = LinkedList.ListNode(0)
    current_node = sum_result
    carry_flag = 0

    while a and b:
        carry_flag, reminder = divmod(a.val + b.val + carry_flag, 10)
        current_node.next = LinkedList.ListNode(reminder)
        current_node = current_node.next
        a = a.next
        b = b.next

    remain_list = a if a else b
    while remain_list:
        carry_flag, reminder = divmod(remain_list.val + carry_flag, 10)
        current_node.next = LinkedList.ListNode(reminder)
        current_node = current_node.next
        remain_list = remain_list.next

    if carry_flag > 0:
        current_node.next = LinkedList.ListNode(carry_flag)
    return sum_result.next


def sum_lists(a, b):
    a_val = 0
    while a:
        a_val = a_val * 10 + a.val
        a = a.next
    b_val = 0
    while b:
        b_val = b_val * 10 + b.val
        b = b.next
    sum_val = a_val + b_val
    head = LinkedList.ListNode(0)
    while sum_val != 0:
        tmp = LinkedList.ListNode(sum_val % 10)
        tmp.next = head.next
        head.next = tmp
        sum_val = sum_val // 10
    return head.next

a = LinkedList.list_to_link_list([7, 1, 6])
b = LinkedList.list_to_link_list([5, 9, 2])
result = sum_lists_reversed(a.head, b.head)
assert LinkedList.compare_linked_list_with_list(result, [2, 1, 9])
a = LinkedList.list_to_link_list([6, 1, 7])
b = LinkedList.list_to_link_list([2, 9, 5])
result = sum_lists(a.head, b.head)
assert LinkedList.compare_linked_list_with_list(result, [9, 1, 2])
