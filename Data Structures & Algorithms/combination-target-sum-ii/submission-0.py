class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0:
            return None
        out = []
        for i in range(len(candidates)):
            result = self.combinationSum2(candidates[i+1:], target-candidates[i])
            if result:
                out += [[candidates[i]] + res for res in result]
        output = []
        visited = set()
        for combo in out:
            if (frozenset(combo), len(combo)) in visited:
                continue
            output.append(combo)
            visited.add((frozenset(combo), len(combo)))
        
        return output
            