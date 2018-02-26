class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [1] + [0 for _ in range(len(s))]
        for i in range(1, len(s) + 1):
            for j in range(len(dp)):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = 1
        # print(dp)
        return bool(dp[-1])