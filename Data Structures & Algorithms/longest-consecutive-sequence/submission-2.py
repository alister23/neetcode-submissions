class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = []
        continues = set()
        for num in nums:
            if num-1 not in set(nums):
                starts.append(num)
            if num+1 in set(nums):
                continues.add(num)
        longest = 0
        for num in starts:
            sequence = 1
            i = num
            while i in continues:
                sequence += 1
                i += 1
            longest = max(longest, sequence)
        return longest
