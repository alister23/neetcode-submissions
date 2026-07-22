class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        chars = set()
        longest = 0
        while right < len(s):
            if s[right] in chars:
                while s[left] != s[right]:
                    chars.remove(s[left])
                    left += 1
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            longest = max(longest, right-left+1)
            right += 1

        return longest