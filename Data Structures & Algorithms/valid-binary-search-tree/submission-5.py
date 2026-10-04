# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # track max left and min right = inorder traversal
        if not root.left and not root.right:
            return True

        def trackBST(root, lower_bound, upper_bound):
            if (lower_bound >= root.val or root.val >= upper_bound):
                return False
            elif not root.left and not root.right:
                return True

            if root.left:
                left_side = trackBST(root.left, lower_bound, min(root.val, upper_bound))
                if not left_side:
                    return False
            if root.right:
                right_side = trackBST(root.right, max(root.val, lower_bound), upper_bound)
                if not right_side:
                    return False

            return True
        
        return trackBST(root, -float("infinity"), float("infinity"))