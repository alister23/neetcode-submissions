# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        cur = new_head
        cur_1 = l1
        cur_2 = l2
        carry = 0
        while cur_1 or cur_2:
            if cur_1:
                cur_1_val = cur_1.val
            else:
                cur_1_val = 0
            if cur_2:
                cur_2_val = cur_2.val
            else:
                cur_2_val = 0
            total = cur_1_val + cur_2_val + carry
            cur.val = total % 10
            carry = total // 10
            if cur_1:
                cur_1 = cur_1.next
            if cur_2:
                cur_2 = cur_2.next
            if cur_1 or cur_2 or carry:
                cur.next = ListNode()
                cur = cur.next
        if carry:
            cur.val = carry
        return new_head