# Note that set in python is hash, looking up in set is O(1)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        
        for num in nums:
            if num - 1 not in nums:
                cur_len = 1
                
                while num + 1 in nums:
                    cur_len += 1
                    num += 1
                
                max_len = max(max_len, cur_len)
        
        return max_len