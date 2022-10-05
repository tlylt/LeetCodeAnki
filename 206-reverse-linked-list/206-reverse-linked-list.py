# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        return self.helper(head, None)
    def helper(self, curr, prev):
        if not curr:
            return prev
        temp = curr.next
        curr.next = prev
        return self.helper(temp, curr)