#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Evaluates a boolean binary tree and returns the result.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            bool: The result of evaluating the boolean binary tree.

        """
        # Base Cases
        if root.val == 1 or root.val == 0:
            return root.val

        # Recursive Cases
        if root.val == 3:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        
        
# @lc code=end

