# dfs
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, path, index = [], [], 0
        candidates.sort()
        self.dfs(candidates, target, index, path, res)
        return res

    def dfs(self, candidates, target, index, path, res):
        if target == 0:
            res.append(path)
        elif target > 0:
            for i in range(index, len(candidates)):
                self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)

# faster dfs
class Solution(object):
    def combinationSum(self, candidates, target):
        def recur(candidates, target, res, pre):
            for i in xrange(len(candidates)):
                if target < candidates[i]: break
                elif target == candidates[i]:
                    res.append(pre + [target])
                else:
                    recur(candidates[i:], target - candidates[i], res, pre + [candidates[i]])
        res = []
        candidates.sort()
        recur(candidates, target, res, [])
        return res

# dp
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[[]]] + [[] for _ in range(target)]
        for cur_target in range(1, len(dp)):
            for num in candidates:
                if num > cur_target:
                    continue
                for path in dp[cur_target - num]:
                    if not path or num >= path[-1]:
                        dp[cur_target].append(path + [num])
        return dp[target]
