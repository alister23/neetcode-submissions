class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.setdefault(num, 0) + 1
        
        freqs_tuple = list(freqs.items())
        freqs_tuple.sort(key=lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(freqs_tuple[i][0])

        return output