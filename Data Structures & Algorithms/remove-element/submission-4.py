class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0

        j = len(nums)-1
        i = 0

        while i <= j:
            if nums[i] == val:
                while j > i and nums[j] == val:
                    j -= 1
                    counter += 1
                nums[i] = nums[j]
                nums[j] = val
                j -= 1
                counter += 1
            
            i += 1
        
        print(nums)
        return len(nums) - counter

        