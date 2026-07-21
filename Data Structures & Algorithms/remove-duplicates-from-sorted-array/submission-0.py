class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        right = len(nums)
        left = 0
        while left < right-1:
            while nums[left] == nums[left+1] and left < right-1:
                j = left + 1
                while j < right-1:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    j += 1
                right -= 1
                count += 1
            left += 1

        return len(nums)-count