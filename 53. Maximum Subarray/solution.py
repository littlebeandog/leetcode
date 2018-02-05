class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-2147483647] + [0] * len(nums)
        for i in range(len(nums)):
            dp[i + 1] = dp[i] + nums[i] if dp[i] >0 else nums[i]
        return max(dp)