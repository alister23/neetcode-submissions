class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        index = 0
        for temp in temperatures:
            if not stack or stack[-1][0] >= temp:
                stack.append((temp, index))
                index += 1
            else:
                while stack and stack[-1][0] < temp:
                    output[stack[-1][1]] = index-stack[-1][1]
                    stack.pop()
                stack.append((temp, index))
                index += 1
        return output