class Solution:
    def binarySearch(nums, target):
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while left <= right:
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            mid = (left+right)//2
        return left


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = nums[:k]
        out = []
        window.sort()
        for i in range(len(nums)-k+1):
            print("sorted window beginning at",i,'is',window)
            out.append(window[-1])
            if i == len(nums)-k:
                break
            delete = Solution.binarySearch(window, nums[i])
            print(f"deleting {nums[i]} at index {delete}")
            del window[delete]
            print(window)
            add = Solution.binarySearch(window, nums[i+k])
            print(f"trying to add {nums[i+k]} at index {add}")
            if add >= len(window):
                print("appending")
                window.append(nums[i+k])
            elif window[add-1] > nums[i+k]:
                print("left too far! adding at add-1")
                left = max(0,add-1)
                print(window[:left], [nums[i+k]], window[left:])
                window = window[:left] + [nums[i+k]] + window[left:]
            else:
                print("adding")
                print(window[:add], [nums[i+k]], window[add+1:])
                window = window[:add] + [nums[i+k]] + window[add:]
        return out
