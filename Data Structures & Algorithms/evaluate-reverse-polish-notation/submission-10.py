class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        out = 0
        stack = []
        for token in tokens:
            # print(stack)
            if token not in operators:
                stack.append(token)
            else:
                operation = token
                right = int(stack.pop())
                left = int(stack.pop())
                # print(left, operation, right)
                if operation == '+':
                    out = left+right
                elif operation == '-':
                    out = left-right
                elif operation == '*':
                    out = left*right
                elif operation == '/':
                    out = int(left / right)
                stack.append(out)
        return int(stack[0])