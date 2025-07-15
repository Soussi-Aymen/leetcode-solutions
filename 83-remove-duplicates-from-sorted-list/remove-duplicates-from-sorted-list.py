# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 

        current = head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next

        return head