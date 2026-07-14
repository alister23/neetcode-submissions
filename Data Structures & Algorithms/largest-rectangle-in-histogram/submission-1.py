class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_extend = [0]*len(heights)
        right_extend = [0]*len(heights)
        left_stack = []
        right_stack = []
        for i in range(len(heights)):
            while left_stack and heights[left_stack[-1]] > heights[i]:
                top = left_stack.pop()
                left_extend[top] = i-top-1
            left_stack.append(i)
        for i in left_stack:
            left_extend[i] = len(heights)-i-1
        for i in range(len(heights)-1,-1,-1):
            while right_stack and heights[right_stack[-1]] > heights[i]:
                top = right_stack.pop()
                right_extend[top] = top-i-1
            right_stack.append(i)
        for i in right_stack:
            right_extend[i] = i
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i]*(1+left_extend[i]+right_extend[i]))
        return max_area
        
