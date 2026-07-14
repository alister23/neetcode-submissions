class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "": return ""

        prefix = ""
        i = 0

        while i < len(strs[0]):
            char = strs[0][i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            prefix += char
            i += 1

        return prefix
