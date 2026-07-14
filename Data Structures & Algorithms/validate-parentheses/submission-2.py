class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        opener = {'(', '{', '['}
        stack = []
        for char in s:
            if char in opener:
                stack.append(char)
            else:
                if not stack:
                    return False
                if pairs[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return not stack