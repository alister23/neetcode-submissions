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

        while cur_1 and cur_2:
            cur_node.next = cur_1
            cur_node = cur_node.next
            cur_1 = cur_1.next
            cur_node.next = cur_2
            cur_node = cur_node.next
            cur_2 = cur_2.next
        
        if cur_1:
            cur_node.next = cur_1
        elif cur_2:
            cur_node.next = cur_2
        
        return head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = head
        previous = None
        future = None
        while cur_node:
            future = cur_node.next
            cur_node.next = previous
            previous = cur_node
            cur_node = future
        
        return previous

    def reorderList(self, head: Optional[ListNode]) -> None:
        counter = 0
        cur_node = head
        while cur_node:
            counter += 1
            cur_node = cur_node.next
        index = 0
        cur_node = head
        mid = None
        while cur_node:
            if index == counter // 2-1:
                mid = cur_node.next
                cur_node.next = None
                break
            index += 1
            cur_node = cur_node.next
        last = self.reverseList(mid)
        # cur_node = head
        # while cur_node:
        #     print(cur_node.val)
        #     cur_node = cur_node.next
        # print("")
        # cur_node = last
        # while cur_node:
        #     print(cur_node.val)
        #     cur_node = cur_node.next

        head = self.mergeTwoLists(head, last)

        

        