class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char)-97] += 1
            freqs.setdefault(tuple(freq), []).append(string)
        return list(freqs.values())