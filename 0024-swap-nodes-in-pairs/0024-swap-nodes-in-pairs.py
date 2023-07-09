# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next and curr.next.next:
            temp = curr.next
            temp1 = curr.next.next.next
            
            curr.next = curr.next.next
            curr.next.next = temp
            temp.next = temp1
            curr = curr.next.next
        return dummy.next