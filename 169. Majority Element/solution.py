class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority, majority_cnt = nums[0], 0
        for num in nums:
            if majority_cnt:
                if num == majority:
                    majority_cnt += 1
                else:
                    majority_cnt -= 1
            else:
                majority_cnt += 1
                majority = num
        return majority