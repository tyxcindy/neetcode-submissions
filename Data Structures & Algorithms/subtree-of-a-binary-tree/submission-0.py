# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        queue_same = []
        queue_find_same_nodes = [root]
        while queue_find_same_nodes:
            node = queue_find_same_nodes.pop(0)
            if node.val == subRoot.val:
                queue_same.append(node)

            if node.left:
                queue_find_same_nodes.append(node.left)
            if node.right:
                queue_find_same_nodes.append(node.right)

        while queue_same:
            test = queue_same.pop()
            if (self.isSameTree(test, subRoot)):
                return True
        
        return False

    def isSameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return ((self.isSameTree(root1.left, root2.left)) and
                (self.isSameTree(root1.right, root2.right)))