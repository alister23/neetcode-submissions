class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set(nums[:k])
        if len(window) != k: return True
        for i in range(k, len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            window.remove(nums[i-k])

        return False