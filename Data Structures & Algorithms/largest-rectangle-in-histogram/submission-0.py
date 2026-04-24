class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                hight = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, hight * width)
            stack.append(i)
        return max_area
