from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = list(freq.items())
        freq.sort(key = lambda x: x[1], reverse=True)
        out = []
        for i in range(k):
            out.append(freq[i][0])

        return out