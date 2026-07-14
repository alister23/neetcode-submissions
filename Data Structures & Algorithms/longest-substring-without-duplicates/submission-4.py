class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        counter = 1
        max_len = 1
        indices = {s[0]: 0}
        seen = {s[0]}
        for i in range(1,len(s)):
            if s[i] in seen:
                counter = i-indices[s[i]]
                seen = set(s[indices[s[i]]+1:i+1])
                indices[s[i]] = i
            else:
                counter += 1
                seen.add(s[i])
                indices[s[i]] = i
            max_len = max(max_len, counter)
        return max_len
