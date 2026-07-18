class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left_prod = 1
        right = [0] * len(nums)
        right_prod = 1

        for i in range(len(nums)):
            left.append(left_prod)
            left_prod *= nums[i]
            right[len(nums)-1-i] = right_prod
            right_prod *= nums[len(nums)-1-i]

        # print(left)
        # print(right)

        out = [0] * len(nums)
        for i in range(len(nums)):
            out[i] = left[i] * right[i]

        return out