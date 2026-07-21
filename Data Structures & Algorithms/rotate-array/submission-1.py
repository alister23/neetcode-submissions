class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen = set()
        for i in range(len(nums)):
            #print(nums)
            # if i has already been considered before
            if i in seen:
                #print(i+1, "th position has already been done")
                continue
            seen.add(i)
            l = i   # the place to get number from
            j = (i+k) % len(nums)   # the place to put number
            n = nums[l]  # the number being put down next cycle
            while i != j:
                seen.add(j)
                temp = nums[j]  # pick up the number from next spot
                #print("putting", n, "where", temp, "was")
                nums[j] = n  # put down the old one
                n = temp    # hold the new one in hand
                l = j
                j = (j+k) % len(nums)
                #print(nums)
            #print("finishing by putting", n, "in the", i+1, "th position")
            nums[i] = n

        

        