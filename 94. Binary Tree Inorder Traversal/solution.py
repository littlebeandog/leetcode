# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traversal(root, res)
        return res
    
    def traversal(self, root, res):
        if not root:
            return
        else:
            self.traversal(root.left, res)
            res.append(root.val)
            self.traversal(root.right, res)

# iter
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop(-1)
                res.append(root.val)
                root = root.right
        return res