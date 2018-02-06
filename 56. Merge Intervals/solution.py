class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda interval: interval.start)
        res = []
        for i in range(len(intervals)):
            if not res or intervals[i].start > res[-1].end:
                res.append(intervals[i])
            else:
                res[-1].end = max(intervals[i].end, res[-1].end)
        return res