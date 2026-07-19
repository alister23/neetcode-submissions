class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while j < n:
            #print("inserting", nums2[j])
            #print(f"{i=} {j=}")
            while i < m+j and nums1[i] < nums2[j]:
                i += 1
            #print(f"inserting {i=}")
            k = m+j
            while k > i:
                nums1[k] = nums1[k-1]
                nums1[k-1] = 0
                k -= 1

            #print(nums1)

            nums1[i] = nums2[j]
            j += 1

            #print(nums1)

        