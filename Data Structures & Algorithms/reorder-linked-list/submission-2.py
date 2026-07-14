# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        if length <= 1:
            return
        second = head
        prev = ListNode()
        for i in range(math.ceil(length/2)-1):
            second = second.next
            previous = second
        cur = second.next
        if cur:
            n = cur.next
            cur.next = None
            previous.next = None
            prev = cur
            cur = n
        while cur:
            n = cur.next
            cur.next = prev
            prev = cur
            cur = n
        cur1 = head
        cur2 = prev
        cur = ListNode()
        while cur1 and cur2:
            print("adding",cur1.val)
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next
            print("adding",cur2.val)
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
            if cur1:
                print("next in line 1:", cur1.val)
            else:
                print("first half DONE")
            if cur2:
                print('next in line 2:', cur2.val)
            else:
                print("second half DONE")
        if cur1:
            cur1.next = None
            cur.next = cur1


        