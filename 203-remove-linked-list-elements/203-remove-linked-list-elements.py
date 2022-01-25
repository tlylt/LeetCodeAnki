# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        while curr:
            while curr and curr.val == val:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr:
                curr = curr.next
        return dummy.next