# recursive
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traversal(root, None, None)

    def traversal(self, root, botom, top):
        if not root:
            return True
        else:
            if botom is not None and root.val <= botom or top is not None and root.val >= top:
                return False
            return (self.traversal(root.left, botom, root.val) and self.traversal(root.right, root.val, top))