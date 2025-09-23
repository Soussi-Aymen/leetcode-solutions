# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        # queue holds (node, lower_bound, upper_bound)
        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, low, high = queue.popleft()
            if not (low < node.val < high):
                return False
            
            if node.left:
                queue.append((node.left, low, node.val))
            if node.right:
                queue.append((node.right, node.val, high))

        return True