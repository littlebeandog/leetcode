# explaination: https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1] + [0 for _ in range(n - 1)]
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]