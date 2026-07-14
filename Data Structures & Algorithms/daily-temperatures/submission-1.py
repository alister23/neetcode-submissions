class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = [len(temperatures)-1]
        for i in range(len(temperatures)-2, -1, -1):
            # print(i, temperatures[i])
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                # print(stack)
                j = stack.pop()
            # print(stack)
            if stack:
                out[i] = stack[-1]-i
            # print(out)
            stack.append(i)
        return out
