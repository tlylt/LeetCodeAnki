# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA and not headB:
            return None
        if headA == headB:
            return headA
        l = headA
        r = headB
        while l != r:
            l = l.next if l else headB
            r = r.next if r else headA
        return l