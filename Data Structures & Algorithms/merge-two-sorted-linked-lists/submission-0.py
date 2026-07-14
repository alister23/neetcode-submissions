# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2

        head = ListNode()
        cur_node = head

        while cur_1 or cur_2:
            if cur_1 and cur_2:
                if cur_1.val < cur_2.val:
                    cur_node.next = cur_1
                    cur_1 = cur_1.next
                else:
                    cur_node.next = cur_2
                    cur_2 = cur_2.next
            elif cur_1:
                cur_node.next = cur_1
                cur_1 = cur_1.next
            else:
                cur_node.next = cur_2
                cur_2 = cur_2.next
            # print(cur_node.val) 
            cur_node = cur_node.next
        
        return head.next
        
