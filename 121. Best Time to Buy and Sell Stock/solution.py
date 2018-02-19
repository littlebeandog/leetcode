class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res, buy = 0, prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            res = max(res, prices[i] - buy)
        return res