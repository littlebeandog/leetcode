# dfs
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path, res = [], []
        self.dfs(nums, path, res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[0: i] + nums[i + 1:], path + [nums[i]], res)

