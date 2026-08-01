class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = []
            heights.append(0)
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i
                    max_area = max(max_area, height * width)
                stack.append(i)
            heights.pop()
        return max_area
        