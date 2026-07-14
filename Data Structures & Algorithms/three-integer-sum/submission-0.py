class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = {}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                pairs.setdefault(nums[i]+nums[j], []).append([nums[i],nums[j], i, j])
        # print(pairs)
        output = []
        for i in range(len(nums)):
            for pair in pairs.setdefault(-1*nums[i], []):
                if i not in pair[2:]:
                    output.append((*pair[:2], nums[i]))
        real_output = []
        seen = set()
        for triple in output:
            if frozenset(triple) not in seen:
                real_output.append(list(triple))
                seen.add(frozenset(triple))


        return real_output