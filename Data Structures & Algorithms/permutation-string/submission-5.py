from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq = [0] * 26
        for char in s1:
            freq[ord(char)-97] += 1

        window = [0] * 26

        for char in s2[:len(s1)]:
            window[ord(char)-97] += 1

        if window == freq: return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i-len(s1)])-97] -= 1
            window[ord(s2[i])-97] += 1
            if window == freq: return True

        return False
