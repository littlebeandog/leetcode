# stack - super slow version
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [(-1, 1)]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((i, 0))
            else:
                if stack and stack[-1][1] == 0:
                    stack.pop()
                else:
                    stack.append((i, 1))
        stack.append((len(s), 1))
        print(stack)
        max_stack = [stack[i + 1][0] - stack[i][0] - 1 for i in range(len(stack) - 1)]
        print(max_stack)
        return reduce(lambda x, y: max(x, y), max_stack) if max_stack else len(s)

# stack - faster version
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif not stack or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
        if not stack:
            return len(s)
        stack = [-1] + stack + [len(s)]
        max_len = 0
        for i in range(1, len(stack)):
            max_len = max(max_len, stack[i] - stack[i - 1] - 1)
        return max_len

# dp version
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = [0 for _ in range(len(s))]
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':    # case1: [some stuff]()
                    length[i] = length[i - 2] + 2
                elif length[i - 1] > 0 and i - length[i - 1] >= 1 and s[i - length[i - 1] - 1] == '(':
                    length[i] = length[i - 1] + 2 + length[i - length[i - 1] -2]
            max_len = max(max_len, length[i])
        return max_len

# a very neat dp solution: https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, stack = [0 for _ in range(len(s) + 1)], []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    length[i + 1] = length[j] + (i - j + 1)
        return max(length)

# why we need an extra element in length list.
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length, stack = [0 for _ in range(len(s))], []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()
                    length[i] = length[j - 1] + (i - j + 1)
        return max(length + [0])