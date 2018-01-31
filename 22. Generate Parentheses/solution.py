class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = 0
        res = [''] if n else []
        res = self.parenthesis(0, n, res)
        return res

    def parenthesis(self, stack, reserve, res):
        l = []
        if stack == 0 and reserve == 0:
            return res

        if stack >= 2:
            l += self.parenthesis(stack - 2, reserve, [s + '))' for s in res])

        if reserve >= 2:
            l += self.parenthesis(stack + 2, reserve - 2, [s + '((' for s in res])

        if stack > 0 and reserve > 0:
            l += self.parenthesis(stack, reserve - 1, [s + ')(' for s in res])

        if reserve > 0:
            l += self.parenthesis(stack, reserve - 1, [s + '()' for s in res])

        return l