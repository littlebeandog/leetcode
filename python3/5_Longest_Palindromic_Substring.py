# A dp solution inspired by https://discuss.leetcode.com/topic/7144/python-o-n-2-method-with-some-optimization-88ms

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        max_len = 1
        for i in range(len(s)):
            if i - max_len >= 0 and s[i - max_len: i + 1] == s[i - max_len: i + 1][::-1]: # case maxlen + 1
                start = i - max_len
                max_len += 1
            if i - max_len - 1 >= 0 and s[i - max_len - 1: i + 1] == s[i - max_len - 1: i + 1][::-1]: # case maxlen + 2
                start = i - max_len - 1
                max_len += 2
        return s[start: start + max_len]