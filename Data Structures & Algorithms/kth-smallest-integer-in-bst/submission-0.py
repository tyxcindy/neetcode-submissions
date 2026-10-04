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
        
        def inorderTraversal(root):
            if not root:
                return None

            seq = []

            if root.left:
                result = inorderTraversal(root.left)
                if result:
                    seq.extend(result)

            seq.append(root.val)
            
            if root.right:
                result = inorderTraversal(root.right)
                if result:
                    seq.extend(result)

            return seq
        
        seq = inorderTraversal(root)
        
        return seq[k-1]