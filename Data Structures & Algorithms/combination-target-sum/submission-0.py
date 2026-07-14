class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0:
            return None
        out = []
        for num in nums:
            result = self.combinationSum(nums, target-num)
            if result is not None:
                out += [[num] + res for res in result]
        visited = set()
        output = []
        for combo in out:
            if (frozenset(combo), len(combo)) in visited:
                continue
            else:
                output.append(combo)
                visited.add((frozenset(combo),len(combo)))
        return output