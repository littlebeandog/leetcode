# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# iterative version
# inspired by https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        in_pointer, stack, flag, cur = 0, [], 0, TreeNode(0)
        root = cur
        while preorder:
            if stack and stack[-1].val == inorder[in_pointer]:
                cur = stack.pop()
                flag = 1
                in_pointer += 1
            else:
                cur_val = preorder.pop(0)
                if not flag:
                    cur.left = TreeNode(cur_val)
                    cur = cur.left
                    stack.append(cur)
                else:
                    cur.right = TreeNode(cur_val)
                    cur = cur.right
                    stack.append(cur)
                    flag = 0
        return root.left