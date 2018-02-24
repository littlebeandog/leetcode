# recursive 
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.combine(root)
    
    def combine(self, root):
        if root.right and root.left:
            right_root, right_last = self.combine(root.right)
            left_root, left_last = self.combine(root.left)
            left_last.right = right_root
            left_last.left = None
            root.right = left_root
            root.left = None
            return root, right_last
        elif not root.right and not root.left:
            return root, root
        elif root.left:
            left_root, left_last = self.combine(root.left)
            root.right = left_root
            root.left = None
            return root, left_last
        else:
            right_root, right_last = self.combine(root.right)
            root.right = right_root
            root.left = None
            return root, right_last

# simplified version
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self._flatten(root)
    
    def _flatten(self, root):
        left_end, right_end = None, None
        
        if root.left:
            left_start, left_end = self._flatten(root.left)
            left_end.right = root.right
            root.right = left_start
            root.left = None
        
        if root.right:
            right_start, right_end = self._flatten(root.right)
        
        return (root, right_end or left_end or root)
            
# super simplified version https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self._flatten(root, None)
    
    def _flatten(self, root, prev):
        if not root:
            return prev
        prev = self._flatten(root.right, prev)
        prev = self._flatten(root.left, prev)
        root.right = prev
        root.left = None
        return root
