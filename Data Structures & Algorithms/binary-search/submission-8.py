class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        last = -1
        mid = (left + right)//2

        while left <= right and mid != last:
            print("looking at", nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            last = mid
            mid = (left + right)//2
            print(f"{last=} {left=} {right=} {mid=}")

        return -1
