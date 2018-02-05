# time limit exceeded
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.step_over(nums, 0)
        
    def step_over(self, nums, i):
        if i == len(nums) - 1:
            return True
        else:
            for j in range(1, nums[i] + 1):
                if self.step_over(nums, i + j):
                    return True
            return False