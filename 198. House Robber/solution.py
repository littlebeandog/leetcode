class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        return dp[-1]