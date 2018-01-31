class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if stack and stack[-1] == d[ch]:
                    stack = stack[:-1]
                else:
                    return False
        return True if not stack else False
               
# https://discuss.leetcode.com/topic/40897/python-is-this-a-cheating-method-accepted-with-40ms-easy-to-understand-but/5
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False