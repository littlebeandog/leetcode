class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        res = 0
        flag = 1
        on_hold = 0
        nums = dict()
        for j in range(10):
            nums[str(j)] = j
        for i in range(len(s)):
            if s[i] == ' ' and on_hold == 0:
                continue
            if s[i] == '-' and on_hold == 0:
                flag *= -1
                on_hold = 1
                continue
            if s[i] == '+' and on_hold == 0:
                on_hold = 1
                continue
            if s[i] in nums and on_hold == 0:
                on_hold = 1
            if s[i] in nums and on_hold == 1:
                res = res * 10 + nums[s[i]]
            if s[i] not in nums:
                break
        res *= flag
        if res > pow(2, 31) -1:
            return pow(2, 31) - 1
        elif res < -pow(2, 31):
            return -pow(2, 31)
        else:
            return res