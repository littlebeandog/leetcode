# A very elegant solution introduced by https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
# The explanation to this algorithm: https://www.youtube.com/watch?v=VNbkzsnllsU 
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights += [0]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                current_index = stack.pop(-1)
                length = i - stack[-1] - 1
                height = heights[current_index]
                res = max(res, height * length)
            stack.append(i)
        return res