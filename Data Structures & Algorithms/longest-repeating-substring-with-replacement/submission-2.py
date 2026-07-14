# key to O(n) solution is that there are a constant number of english characters
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        freqs = [0]*26
        longest = 0
        while end < len(s):
            freqs[ord(s[end])-65] += 1
            most_common = end-start+1-k
            while max(freqs) < most_common:
                freqs[ord(s[start])-65] -= 1
                start += 1
                most_common = end-start+1-k
            longest = max(longest, end-start+1)
            end += 1
        return longest