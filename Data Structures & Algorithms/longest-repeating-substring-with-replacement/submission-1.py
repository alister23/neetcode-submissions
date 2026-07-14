class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        freqs = {}
        longest = 0
        while end < len(s):
            freqs[s[end]] = freqs.setdefault(s[end],0)+1
            most_common = end-start+1-k
            while max(freqs.values()) < most_common:
                freqs[s[start]] -= 1
                start += 1
                most_common = end-start+1-k
            longest = max(longest, end-start+1)
            end += 1
        return longest