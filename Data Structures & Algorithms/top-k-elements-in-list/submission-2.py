class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        max_freq = max(freq.values())
        # print(freq)
        # print(max_freq)
        freqs = [0]*max_freq
        for num in freq:
            if freqs[freq[num]-1] == 0:
                freqs[freq[num]-1] = []
            freqs[freq[num]-1].append(num)
        output = []
        # print(freqs)
        for i in freqs[::-1]:
            if i:
                output += i
                # print("added", i)
                k -= len(i)
                # print("k is now", k)
                if k <= 0:
                    return output
