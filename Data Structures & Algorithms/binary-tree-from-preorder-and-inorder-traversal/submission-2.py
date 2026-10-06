# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            pre_val = next(pre_iter)
            tree = TreeNode(pre_val)
            index = inorder_idx[pre_val]
            tree.left = helper(left, index - 1)
            tree.right = helper(index + 1, right)
            return tree

        return helper(0, len(inorder) - 1)