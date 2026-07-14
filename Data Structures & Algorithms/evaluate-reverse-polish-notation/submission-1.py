class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif token == "-":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            elif token == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif token == "/":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(token))
            # print(stack)
        return int(stack[0])
            