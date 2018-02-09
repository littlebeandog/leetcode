# dfs
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


# one-line reduce
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda res, num: res + [one_res + [num] for one_res in res], nums, [[]])