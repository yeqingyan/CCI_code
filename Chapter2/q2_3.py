""" Question 2.3 """
from LinkedList import *


def delete_middle_node(remove_node):
    """ delete middle node  """
    next_node = remove_node.next
    remove_node.val = next_node.val
    remove_node.next = next_node.next

link_list = LinkedList.create_random_linklist(1, 100, 10)
i = link_list.get_node(5)
link_list.print()
delete_middle_node(i)
link_list.print()


