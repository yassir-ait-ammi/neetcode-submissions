"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        curr = head
        new_list = None
        curr_list = None
        while curr:
            new_node = Node(curr.val)
            old_to_new[curr] = new_node
            if new_list is None:
                new_list = new_node
                curr_list = new_node
            else:
                curr_list.next = new_node
                curr_list = new_node
            curr = curr.next
        curr_list = new_list
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr_list.random = old_to_new[curr.random]
            curr = curr.next        
            curr_list = curr_list.next
        return new_list  