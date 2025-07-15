# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head  # Initialize previous as None, current as head

        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev  # Reverse the link
            prev = curr  # Move prev pointer forward
            curr = next_node  # Move current pointer forward
        
        return prev  # New head of the reversed list