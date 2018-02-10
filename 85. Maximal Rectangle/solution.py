# Convert to largest rectangle in histogram

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        heights = [0 for _ in range(len(matrix[0]))]
        res = 0
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                print(matrix[row][column])
                heights[column] = 0 if matrix[row][column] == '0' else (heights[column] + 1)
            res = max(res, self.max_rectangle_histogram(heights))
        return res

    def max_rectangle_histogram(self, heights):
        stack = [-1]
        heights = heights + [0]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                current_index = stack.pop(-1)
                length = i - stack[-1] - 1
                height = heights[current_index]
                res = max(res, length * height)
            stack.append(i)
        return res

# dp?
