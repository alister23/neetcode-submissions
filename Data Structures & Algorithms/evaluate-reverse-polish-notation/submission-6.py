class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def evalRPNrecur(tokens, index):
            operation = tokens[index]
            # print(operation)
            if tokens[index-1].isdigit() or (tokens[index-1][0] == "-" and tokens[index-1][1:].isdigit()):
                operand2 = int(tokens[index-1])
                index -= 1
            else:
                operand2, index = evalRPNrecur(tokens, index-1)
            # print("operand2", operand2)
            if tokens[index-1].isdigit() or (tokens[index-1][0] == "-" and tokens[index-1][1:].isdigit()):
                operand1 = int(tokens[index-1])
                index -= 1
            else:
                operand1, index = evalRPNrecur(tokens, index-1)
            # print("operand1", operand1)
            output = None
            if operation == "+":
                output = operand1+operand2
            elif operation == "-":
                output = operand1-operand2
            elif operation == "*":
                output = operand1*operand2
            elif operation == "/":
                output = int(operand1/operand2)
            return (output, index)
        return evalRPNrecur(tokens, len(tokens)-1)[0]
            