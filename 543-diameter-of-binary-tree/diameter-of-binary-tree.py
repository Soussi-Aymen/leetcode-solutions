# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_diameter = dfs(node.left)
            right_diameter = dfs(node.right)
            self.diameter = max(self.diameter, left_diameter + right_diameter)
            
            return 1 + max(left_diameter, right_diameter)
            
        dfs(root)
        return self.diameter