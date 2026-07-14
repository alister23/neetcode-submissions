class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                processed += char.lower()
        left = 0
        right = len(processed)-1
        while left < right:
            if processed[left] != processed[right]:
                return False
            left += 1
            right -= 1
        return True