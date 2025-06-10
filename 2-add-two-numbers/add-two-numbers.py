# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        current = node
        rest = 0
        while l1 or l2 or rest:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = (val1 + val2 + rest) % 10
            rest = (val1 + val2 + rest) // 10
            current.next = ListNode(val)
            current = current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return node.next
        