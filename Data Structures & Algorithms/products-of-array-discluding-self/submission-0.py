class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]*len(nums)
        prefix_product = 1
        for i in range(0,len(nums)-1):
            prefix_product *= nums[i]
            prefixes[i+1] = prefix_product
        
        suffixes = [1]*len(nums)
        suffix_product = 1
        for i in range(len(nums)-1,0,-1):
            suffix_product *= nums[i]
            suffixes[i-1] = suffix_product
        
        # print(prefixes)
        # print(suffixes)
        output = []
        for i in range(len(nums)):
            output.append(prefixes[i]*suffixes[i])
        
        return output