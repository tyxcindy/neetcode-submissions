# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        original = root

        queue = [root]
        while queue:
            current = queue.pop(0)

            # Add children to queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            saved = current.left
            current.left = current.right
            current.right = saved

        return original