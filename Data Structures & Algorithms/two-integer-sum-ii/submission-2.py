class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        candidates = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if target-num in candidates:
                return [candidates[target-num]+1, i+1]
            if num not in candidates:
                candidates[num] = i
            else:
                del candidates[num]