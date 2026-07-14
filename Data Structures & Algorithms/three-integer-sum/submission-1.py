class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        two_sum = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                two_sum[nums[i] + nums[j]] = two_sum.setdefault(nums[i]+nums[j],set())
                two_sum[nums[i] + nums[j]].add((i,j))
        
        triplets = set()
        for k in range(len(nums)):
            target = -1*nums[k]
            if target in two_sum:
                for i,j in two_sum[target]:
                    if i == k or j == k:
                        continue
                    triplet = [nums[i], nums[j], nums[k]]
                    triplet.sort()
                    triplets.add(tuple(triplet))
        
        return list(list(triplet) for triplet in triplets)