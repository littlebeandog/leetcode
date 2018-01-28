class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s, e = 0, len(height) - 1
        start, end = s , e
        while s < e:
            if height[s] <= height[e]:
                s += 1
            else:
                e -= 1
            if min(height[s], height[e]) * (e - s) > min(height[start], height[end]) * (end - start):
                start, end = s, e
        return min(height[start], height[end]) * (end - start)
            
            
            
        