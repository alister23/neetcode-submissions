class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        freq1 = {}
        freq2 = {}
        for i in range(len(s)):
            freq1[s[i]] = freq1.setdefault(s[i], 0) + 1
            freq2[t[i]] = freq2.setdefault(t[i],0) + 1
        return freq1 == freq2