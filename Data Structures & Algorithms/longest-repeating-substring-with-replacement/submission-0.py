class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freqs = [0]*26
        j = 0
        for i in range(len(s)):
            freqs[ord(s[i])-ord('A')] += 1
            while i-j+1-max(freqs) > k:
                # print(freqs)
                freqs[ord(s[j])-ord('A')] -= 1
                j += 1
            max_len = max(max_len, i-j+1)
        return max_len
            