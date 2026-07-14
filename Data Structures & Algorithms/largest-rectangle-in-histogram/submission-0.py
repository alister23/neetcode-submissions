class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        boundaries = [[0,0] for _ in range(len(heights))]
        stack = [(0, heights[0])]
        heights = list(enumerate(heights))
        for index, height in heights[1:]:
            while stack and height < stack[-1][1]:
                boundaries[stack[-1][0]][1] = index
                stack.pop()
            if stack:
                boundaries[index][0] = stack[-1][0]+1
            stack.append((index, height))
        for index, _ in stack:
            boundaries[index][1] = len(heights)
        print(boundaries)
        
        max_area = 0
        for index, height in heights:
            max_area = max(max_area, height*(boundaries[index][1]-boundaries[index][0]))
        return max_area
            
