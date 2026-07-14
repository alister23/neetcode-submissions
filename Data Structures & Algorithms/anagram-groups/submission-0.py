class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freqs = {}
            for char in string:
                freqs[char] = freqs.setdefault(char, 0) + 1
            anagrams.setdefault(frozenset(freqs.items()), []).append(string)
        return list(anagrams.values())