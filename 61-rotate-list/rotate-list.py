# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head

        while tail.next:
            n += 1
            tail = tail.next

        k = k % n
        if k == 0:
            return head
        
        tail.next = head
        new_tail = head
        steps_to_new_head = n - k

        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        new_tail.next = None

        return new_head

