class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "ç"
        if strs == [""]:
            return ""
        output = ""
        for string in strs:
            output += string + "ç"
        return output[:-1]

    def decode(self, s: str) -> List[str]:
        if s == "ç":
            return []
        return s.split("ç")
