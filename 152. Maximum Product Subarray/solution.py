class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur_min = cur_max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_min = min(nums[i], nums[i] * cur_min)
            cur_max = max(nums[i], nums[i] * cur_max)
        
            res = max(cur_max, res)
        
        return res