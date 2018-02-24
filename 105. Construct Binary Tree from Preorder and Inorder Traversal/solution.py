# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive version
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, inorder, 0, len(preorder))

    def build(self, preorder, inorder, left_idx, right_idx):
        if left_idx < right_idx:
            root = TreeNode(preorder[0])
            root_idx = inorder.index(preorder[0])
            preorder.pop(0)
            root.left = self.build(preorder, inorder, left_idx, root_idx)
            root.right = self.build(preorder, inorder, root_idx + 1, right_idx)
            return root
        else:
            return None