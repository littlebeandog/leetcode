# Time limit exceeded
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water, length = 0, len(height)
        if not height:
            return 0
        while max(height):
            height = list(map(lambda x: x - 1, height))
            left, right = 0, 0
            for i in range(0, length):
                if height[i] >= 0:
                    left = i
                    break
            for i in range(length - 1, -1, -1):
                if height[i] >= 0:
                    right = i
                    break
            for i in range(left + 1, right):
                if height[i] <= -1:
                    water += 1
        return water

# Time limit exceeded
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        water, max_height = 0, max(height)
        left_wall = [0 for _ in range(max_height + 1)]
        for i in range(len(height)):
            for h in range(1, height[i] + 1):
                if left_wall[h]:
                    water += i - left_wall[h]
                    left_wall[h] = i + 1
                left_wall[h] = i + 1
        return water

# dp solution 1: keep track of water level
# dp solution 1: Keeping track of the highest water level
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        level, volume = 0, 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > level:
                    volume += (right - left - 1) * (height[left] - level) - level
                    level = height[left]
                else:
                    volume -= height[left]
                left += 1
            else:
                if height[right] > level:
                    volume += (right - left - 1) * (height[right] - level) - level
                    level = height[right]
                else:
                    volume -= height[right]
                right -= 1
        return volume

# dp2: calculate each bin on one move
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_left, max_right, water = 0, 0, 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] < max_left:
                    water += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    water += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return water