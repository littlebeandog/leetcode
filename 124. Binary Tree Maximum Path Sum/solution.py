# recursive

class Solution(object):
    res = None
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val
        self.max_path_sum(root)
        return self.res
    
    def max_path_sum(self, root):
        if not root:
            return 0
        left_max_sum = self.max_path_sum(root.left)
        right_max_sum = self.max_path_sum(root.right)
        max_with_root = max(left_max_sum + root.val, right_max_sum + root.val, root.val)
        self.res = max(self.res, root.val, root.val + right_max_sum, root.val + left_max_sum, root.val + left_max_sum + right_max_sum)
        return max_with_root
        