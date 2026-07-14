class Solution:
    # binary search for number of elts to take from shorter list
    # check each partition is valid
    # edge case is if length of list is even or odd
    def checkPartition(shorter, longer, amount, half):
        if amount > len(shorter):
            return False
        if amount == len(shorter):
            short_left = shorter[-1]
            short_right = float("inf")
        elif amount == 0:
            short_left = -float("inf")
            short_right = shorter[0]
        else:
            short_left = shorter[amount-1]
            short_right = shorter[amount]
        if amount == half:
            long_left = -float("inf")
            long_right = longer[0]
        elif half-amount == len(longer):
            long_left = longer[half-amount-1]
            long_right = float("inf")
        else:
            long_left = longer[half-amount-1]
            long_right = longer[half-amount]
        if min(short_right, long_right) >= max(short_left, long_left):
            return (max(short_left, long_left), min(short_right, long_right))
        else:
            if short_left > short_right:
                return "left"
            else:
                return "right"
            
        

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        shorter = []
        longer = []
        total_len = len(nums1) + len(nums2)
        half = total_len//2
        if len(nums1) < len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1
        print("finding median with",len(shorter),"elements in shorter list and",len(longer),"elements in longer list")
        left = 0
        right = len(shorter)-1
        mid = (left+right)//2
        while left <= right:
            print("trying to take",mid,"elements form shorter list")
            check = Solution.checkPartition(shorter, longer, mid, half)
            if check not in {'left', 'right'}:
                bottom, top = check
                if total_len%2 == 1:
                    return top
                else:
                    return (top+bottom)/2
            else:
                if check == 'left':
                    right = mid-1
                else:
                    left = mid+1
                mid = (left+right)//2
        if len(longer)%2 == 1:
            return longer[len(longer)//2]
        else:
            return (longer[len(longer)//2]+longer[len(longer)//2-1])/2
        
