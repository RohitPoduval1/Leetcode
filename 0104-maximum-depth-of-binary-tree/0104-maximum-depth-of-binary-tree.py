# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case (simplest case)
        if root is None:
            return 0
        
        # `1 +` because the current level contributes to the depth
        # `self.maxDepth(child)` because one child could be shallow but the
        # other child could be deep. We want the largest depth of both children
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))