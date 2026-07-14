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
        cur = head
        nodes = {}
        nodes[None] = None
        while cur:
            newNode = Node(cur.val,None)
            nodes[cur] = newNode
            cur = cur.next
        cur = head
        while cur:
            nodes[cur].next = nodes[cur.next]
            nodes[cur].random = nodes[cur.random]
            cur = cur.next
        return nodes[head]