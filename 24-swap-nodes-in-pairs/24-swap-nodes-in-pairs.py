# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy
        while curr and curr.next:
            temp = curr.next.next
            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp
            prev = curr
            curr = temp
        return dummy.next
