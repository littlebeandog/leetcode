class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        for i in range(len(s)):
            row = i % (numRows - 1) if int(i / (numRows - 1)) % 2 == 0 else numRows - 1 - i % (numRows - 1)
            res[row].append(s[i])
        return "".join(["".join(l) for l in res])