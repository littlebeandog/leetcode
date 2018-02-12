class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root] if root else []
        res = []
        while queue:
            res.append([node.val for node in queue])
            queue = [node for parent in queue for node in (parent.left, parent.right) if node]
        return res