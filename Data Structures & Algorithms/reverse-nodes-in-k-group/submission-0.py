# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None, None
            cur_node = head
            last_node = None
            i = 0
            while i < k:
                next_node = cur_node.next
                cur_node.next = last_node
                last_node = cur_node
                cur_node = next_node
                i += 1
            return last_node, head

        # def get(node):
        #     if node:
        #         return node.val
        #     return None

        n = 0
        cur_node = head
        while cur_node:
            n += 1
            cur_node = cur_node.next
        q = n // k
        cur_node = head
        out = None
        prev = None
        for _ in range(q):
            # print('previous node:', get(prev))
            # print('starting at', get(cur_node))
            it = cur_node
            for _ in range(k):
                it = it.next
            next_cur = it
            # print('node after is', get(next_cur))
            front, back = reverseList(cur_node)
            # print('now first node is', get(front), ', last is', get(back))
            if not out:
                out = front
                # print(get(out), 'is now the head node')
            if prev:
                prev.next = front
                # print('attached', get(prev), 'and', get(front))
            prev = back
            cur_node = next_cur
        prev.next = cur_node
        return out
        

        
