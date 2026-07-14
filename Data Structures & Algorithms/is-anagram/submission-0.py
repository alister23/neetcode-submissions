class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = {}
        t_freq = {}
        for i in range(len(s)):
            s_freq[s[i]] = s_freq.setdefault(s[i], 0) + 1
            t_freq[t[i]] = t_freq.setdefault(t[i], 0) + 1
        if s_freq != t_freq:
            return False
        return True