class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for string in strs:
            output += str(len(string))
            output += '.'
            output += string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            length = ''
            while s[i].isdigit():
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            string = s[i:i+length]
            output.append(string)
            i += length
        return output

