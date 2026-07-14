# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = [head for head in lists]
        out_head = ListNode()
        cur = out_head
        while any(heads):
            min_node = ListNode(val=float("inf"))
            min_index = -1
            for i in range(len(heads)):
                if heads[i]:
                    if heads[i].val < min_node.val:
                        min_index = i
                        min_node = heads[i]
            heads[min_index] = min_node.next
            cur.next = min_node
            cur = cur.next
        return out_head.next