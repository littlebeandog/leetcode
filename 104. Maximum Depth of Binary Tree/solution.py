# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max_depth(root, 0)
    
    def max_depth(self, root, depth):
        if not root:
            return depth
        else:
            return max(self.max_depth(root.left, depth + 1), self.max_depth(root.right, depth + 1))
        