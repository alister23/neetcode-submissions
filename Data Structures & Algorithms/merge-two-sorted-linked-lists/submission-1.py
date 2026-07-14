# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2
        cur = ListNode()
        head = cur
        while cur_1 and cur_2:
            if cur_1.val < cur_2.val:
                # print("attaching", cur_1.val,"from list 1")
                cur.next = cur_1
                cur_1 = cur_1.next
                # if cur_1:
                    # print("head of list 1 is now at", cur_1.val)
            else:
                # print("attaching", cur_2.val,"from list 2")
                cur.next = cur_2
                cur_2 = cur_2.next
                # if cur_2:
                    # print("head of list 2 is now at", cur_2.val)
            cur = cur.next
        if not cur_1:
            # print("ran out of list 1, here is list 2")
            cur.next = cur_2
        if not cur_2:
            # print("ran out of list 2, here is list 1")
            cur.next = cur_1
        return head.next

        