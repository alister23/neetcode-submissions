class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        write = 1
        for new in range(1, len(nums)):
            if nums[new] != nums[new-1]:
                nums[write] = nums[new]
                write += 1
                count += 1

        return count