# inspired by https://discuss.leetcode.com/topic/22705/python-140ms-beats-100-and-works-for-n-sum-n-2

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.n_sum(nums, target, 4, [], res)
        return res

    def n_sum(self, nums, target, n, path, res):
        if n == 2:      # 2 sum problem
            i, j = 0, len(nums) - 1
            while i < j:
                t = nums[i] + nums[j]
                if t == target:
                    res.append(path + [nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif t < target:
                    i += 1
                else:
                    j -= 1
        else:           # n > 2
            for i in range(len(nums) - n + 1):
                # early stop
                if nums[i] * n > target:
                    break
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    self.n_sum(nums[i + 1:], target - nums[i], n - 1, path + [nums[i]], res)