class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = [('(',1,0)]
        visited = set()
        output = []
        while queue:
            string, opening, closing = queue.pop(0)
            if len(string) == 2*n:
                output.append(string)
            else:
                if opening < n:
                    queue.append((string+"(", opening+1, closing))
                    visited.add(string+"(")
                if opening > closing:
                    queue.append((string+")", opening, closing+1))
                    visited.add(string+")")
        return output
            