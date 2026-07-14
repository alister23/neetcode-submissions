# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_slow = head
        cur_fast = head
        while cur_slow and cur_fast:
            cur_slow = cur_slow.next
            cur_fast = cur_fast.next
            if cur_fast:
                cur_fast = cur_fast.next
            else:
                break
            if cur_slow == cur_fast:
                return True
        return False