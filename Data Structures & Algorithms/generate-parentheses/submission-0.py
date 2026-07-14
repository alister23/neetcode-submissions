class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(opening, closing):
            # print("adding parens...")
            if not opening and not closing:
                return [""]
            output = []
            if opening:
                output += ["(" + result for result in generate(opening-1, closing+1)]
            if closing:
                output += [")" + result for result in generate(opening, closing-1)]
            # print(output)
            return output
        return generate(n, 0)

