# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        # Going layer by layer ==> Adding into a "level" (all direct children in one level)
        # Add the "level" into the big traversal
        # Get next "level" queue ready
        
        queue = [[root]]
        traversal = []
        while queue:
            group = queue.pop(0)
            curr_level = []
            next_queue = []
            while group:
                curr = group.pop(0)
                if curr:
                    curr_level.append(curr.val)
                    next_queue.extend([curr.left, curr.right])
            
            if next_queue:
                queue.append(next_queue)
            if curr_level:
                traversal.append(curr_level)

        return traversal
