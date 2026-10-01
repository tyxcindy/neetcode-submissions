# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = [(root, 1)]
        count = 1

        while queue:
            current, depth = queue.pop()

            if current.left:
                queue.append((current.left, depth + 1))
            
            if current.right:
                queue.append((current.right, depth + 1))
            
            if current.left or current.right:
                count = max(count, depth + 1)

        return count

        # Recursion
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth,right_depth)
