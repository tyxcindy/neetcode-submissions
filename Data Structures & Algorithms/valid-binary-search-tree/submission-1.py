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

        def trackBST(root):
            if not root.left and not root.right:
                return (root.val, root.val)
            
            min_val, max_val = root.val, root.val
            if root.left:
                left_min, left_max = trackBST(root.left)
                if left_max >= root.val:
                    return (-float("infinity"), float("infinity"))
                min_val = min(left_min, min_val)
                max_val = max(left_max, max_val)
            if root.right:
                right_min, right_max = trackBST(root.right)
                if right_min <= root.val:
                    return (-float("infinity"), float("infinity"))
                min_val = min(right_min, min_val)
                max_val = max(right_max, max_val)

            return (min_val, max_val)
        
        min_val, max_val = trackBST(root)
        
        if min_val == -float("infinity") and max_val == float("infinity"):
            return False
        
        return True