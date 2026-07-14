# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        cur_node = head
        cur_1 = l1
        cur_2 = l2
        prev = None
        while cur_1 and cur_2:
            cur_node.val = (cur_1.val+cur_2.val+carry)%10
            carry = (cur_1.val+cur_2.val+carry) // 10
            prev = cur_node
            cur_node.next = ListNode()
            cur_node = cur_node.next
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        
        while cur_1:
            cur_node.val = (cur_1.val+carry)%10
            carry = (cur_1.val+carry)//10
            prev = cur_node
            cur_node.next = ListNode()
            cur_node = cur_node.next
            cur_1 = cur_1.next

        while cur_2:
            cur_node.val = (cur_2.val+carry)%10
            carry = (cur_2.val+carry)//10
            prev = cur_node
            cur_node.next = ListNode()
            cur_node = cur_node.next
            cur_2 = cur_2.next
        
        if carry:
            cur_node.val = carry
        else:
            prev.next = None

        return head