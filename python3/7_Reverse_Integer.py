class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        abs_x = abs(x)
        flag = 1 if x == 0 else x/abs_x
        while abs_x:
            res = res * 10 + (abs_x % 10)
            abs_x /= 10
        print(res, abs_x, x)
        res *= flag
        return 0 if res > pow(2, 31)-1 or res < -pow(2, 31) else res
        

# faster version
