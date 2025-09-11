# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        stack = []
        node = head
        
        while node:
            stack.append(node)
            node = node.next
        
        node = head
        n = len(stack)
        for _ in range(n // 2):
            temp = stack.pop()
            new = node.next
            temp.next = new
            node.next = temp
            node = node.next.next

        node.next = None

        return head  

        