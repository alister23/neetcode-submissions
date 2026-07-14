class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char)-97] += 1
            anagrams[tuple(freq)] = anagrams.setdefault(tuple(freq), [])
            anagrams[tuple(freq)].append(string)
        return anagrams.values()