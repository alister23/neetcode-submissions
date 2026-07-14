class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'(','{','['}
        closing = {
            ')': "(",
            '}': '{',
            ']': '['
        }
        stack = []
        for paren in s:
            if paren in opening:
                stack.append(paren)
            elif paren in closing:
                if not stack:
                    return False
                if stack.pop() != closing[paren]:
                    return False
            else:
                return False
        if stack:
            return False
        return True