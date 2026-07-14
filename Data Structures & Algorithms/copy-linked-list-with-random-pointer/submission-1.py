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
        if not head:
            return None
        cur_node = head
        new_head = Node(head.val)
        new_cur = new_head
        nodes = {new_head: head}
        rev_nodes = {head: new_head}

        while cur_node:
            if cur_node.next:
                new_cur.next = Node(cur_node.next.val)
            else:
                new_cur.next = None
            cur_node = cur_node.next
            new_cur = new_cur.next
            nodes[new_cur] = cur_node
            rev_nodes[cur_node] = new_cur

        cur_node = new_head
        while cur_node:
            # print(nodes[cur_node].random)
            cur_node.random = rev_nodes[nodes[cur_node].random]
            cur_node = cur_node.next
        
        return new_head