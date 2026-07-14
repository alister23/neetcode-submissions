class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indices = {}
        start = 0
        end = 0
        longest = 0
        while end < len(s):
            if s[end] in indices and indices[s[end]] >= start:
                start = indices[s[end]]+1
            indices[s[end]] = end
            longest = max(longest, end-start+1)
            print(s[start:end+1])
            end += 1
        return longest

