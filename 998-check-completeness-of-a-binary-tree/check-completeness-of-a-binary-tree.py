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
        # flag to mark if a None has been seen
        end = False 
        
        while queue:
            node = queue.popleft()
            if node:
                if end:
                    # If we have seen None before, any non-null node after is invalid
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Mark that we have encountered a None
                end = True 
        return True