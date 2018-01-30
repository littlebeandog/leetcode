class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = list()
        if len(nums) < 3:
            return []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j - 1] == nums[j]:
                    j += 1
                elif k < len(nums) - 1 and nums[k + 1] == nums[k]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res
            