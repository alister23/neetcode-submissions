class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        diff = 0
        most = 0
        longest = 0

        left = 0
        right = 0

        while right < len(s):
            existing = window.setdefault(s[right], 0)
            if existing == most:
                most += 1
                longest += 1
            else:
                if diff == k:
                    window[s[left]] -= 1
                    left += 1
                else:
                    diff += 1
                    longest += 1
            window[s[right]] += 1
            right += 1

        return longest

        