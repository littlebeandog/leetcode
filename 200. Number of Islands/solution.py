class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        if not grid:
            return cnt
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid, i, j)
        return cnt

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)