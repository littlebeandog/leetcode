class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [i for i in range(len(word2) + 1)]
        for i in range(len(word1)):
            keep = dp[0]
            dp[0] = i + 1
            for j in range(len(word2)):
                tmp = dp[j + 1]
                dp[j + 1] = min(
                    dp[j] + 1,
                    dp[j + 1] + 1,
                    keep + (0 if word1[i] == word2[j] else 1)
                )
                keep = tmp
        return dp[-1] if word2 else len(word1)