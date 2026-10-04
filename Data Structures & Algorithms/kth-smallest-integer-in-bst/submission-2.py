# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return None
        
        seq = []
        
        def inorderTraversal(root):
            nonlocal seq
            if not root:
                return None

            if root.left:
                seq = inorderTraversal(root.left)
                if len(seq) == k:
                    return seq

            seq.append(root.val)

            if len(seq) == k:
                return seq
            
            if root.right:
                seq = inorderTraversal(root.right)
                if len(seq) == k:
                    return seq

            return seq
        
        seq = inorderTraversal(root)
        
        return seq[k-1]