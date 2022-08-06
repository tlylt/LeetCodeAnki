# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        curr_a = headA
        curr_b = headB
        while curr_a != curr_b:
            curr_a = curr_a.next if curr_a else headB
            curr_b = curr_b.next if curr_b else headA
        return curr_a