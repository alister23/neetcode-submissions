from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = [-x for x in nums[:k]]
        heapify(heap)
        todelete = set()
        for i in range(k-1,len(nums)):
            maximum = heap.pop(0)
            while maximum in todelete:
                # print(maximum)
                todelete.remove(maximum)
                heapify(heap)
                maximum = heap.pop(0)
            # print(heap)
            output.append(maximum*-1)
            heappush(heap, maximum)
            # print(heap)
            if i < len(nums)-1:
                todelete.add(-1*nums[i-k+1])
                heappush(heap, -1*nums[i+1])
                # print(heap)
                # print(todelete)
        return output