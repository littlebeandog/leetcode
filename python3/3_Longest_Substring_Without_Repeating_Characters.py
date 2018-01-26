class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        ch_set = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in ch_set:
                ch_set.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                ch_set.remove(s[left])
                left += 1
        return max_len

# faster version
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlen = 0
        start = 0
        trace = {}
        for index, ch in enumerate(s):
            if ch in trace and trace[ch] >= start:
                rlen = max(rlen, index - start)
                start = trace[ch] + 1
            trace[ch] = index
        return max(rlen, len(s) - start)
