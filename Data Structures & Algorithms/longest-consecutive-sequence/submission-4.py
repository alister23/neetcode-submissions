class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = {}
        for num in nums:
            if num-1 not in num_set:
                starts[num] = 1
                i = num+1
                while i in num_set:
                    starts[num] += 1
                    i += 1
        
        if not starts:
            return 0
        return max(starts.values())


            



