class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for string in strs:
            out += "*" + str(len(string)) + "*"
            out += string

        return out

    def decode(self, s: str) -> List[str]:
        print(s)
        out = []
        i = 0
        while i < len(s):
            i += 1
            length = ""
            word = ""
            while s[i] != "*":
                length += s[i]
                i += 1
            length = int(length)
            for _ in range(length):
                i += 1
                word += s[i]
            out.append(word)
            i += 1
            

        return out