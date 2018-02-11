# recursive
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if not root else self.is_mirror(root.left, root.right)
    
    def is_mirror(self, left, right):
        if right and left and right.val == left.val:
            return (self.is_mirror(left.left, right.right) and self.is_mirror(left.right, right.left))
        return left == right

# iter,a concise solution: https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]
        while queue:
            values = [node.val if node else None for node in queue]
            if values[:len(values)/2] != values[:len(values)/2 - 1: -1]:
                return False
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return True