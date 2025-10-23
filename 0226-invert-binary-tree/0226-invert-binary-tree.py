# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverting a binary tree does not just mean the left and right children are swapped, but 
        actually the left and right SUBTREES are swapped, hence the recursive call to
        self.invertTree().

        Time: O(V + E) traverse every node
        """
        if root is None:
            return None

        # The root's children are swapped subtrees
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root