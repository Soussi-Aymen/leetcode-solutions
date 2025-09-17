# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        node = root
        queue = deque([node])
        end = False # flag to mark if a None has been seen
        
        while queue:
            node = queue.popleft()
            if node:
                if end:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
            else:
                end = True
        return True