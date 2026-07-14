# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        cur_node = head
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        
        index = counter - n

        if index == 0:
            return head.next

        i = 0
        cur_node = head
        while i < index - 1:
            cur_node = cur_node.next
            i += 1
        
        next_node = cur_node.next.next
        cur_node.next = next_node

        return head