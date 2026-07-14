class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        out = []
        for i in range(len(nums)):
            res = self.permute(nums[:i]+nums[i+1:])
            out += [[nums[i]]+r for r in res]
        return out