from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        start, end = 0, 0
        min_start, min_end = 0, len(s)
        counter, is_invalid = Counter(t), len(t)
        while end < len(s):
            if counter[s[end]] > 0:
                is_invalid -= 1
            counter[s[end]] -= 1
            if not is_invalid:
                while start < end and counter[s[start]] < 0:
                    counter[s[start]] += 1
                    start += 1
                (min_start, min_end) = (min_start, min_end) if min_end - min_start <= end - start else (start, end)
            end += 1
        return s[min_start:min_end + 1] if min_end != len(s) else ''