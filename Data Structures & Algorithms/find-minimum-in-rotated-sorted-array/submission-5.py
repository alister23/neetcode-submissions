class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        join = -1
        print("searching for break")
        while left <= right:
            print("checking index", mid)
            if mid == len(nums)-1:
                print("found at end")
                join = mid
                break
            elif nums[mid] > nums[mid+1]:
                print("found at index", mid)
                join = mid
                break
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left+right)//2
            print(f"{left=} {right=} {mid=}")
        if join == len(nums)-1:
            return nums[0]
        else:
            return nums[join+1]