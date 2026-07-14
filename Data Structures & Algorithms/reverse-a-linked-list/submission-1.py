# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur_node = head
        last_node = None
        while cur_node:
            new_node = ListNode(val=cur_node.val, next=last_node)
            last_node = new_node
            cur_node = cur_node.next
        return last_node