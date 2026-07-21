class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        out = set()
        for i in range(len(nums)):
            target = -1*nums[i]

            left = 0
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target and left != i and right != i:
                    out.add(tuple(sorted([nums[left], nums[right], -1*target])))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return [list(tup) for tup in out]
