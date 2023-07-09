# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        pt1 = headA
        pt2 = headB
        
        while pt1 != pt2:
            pt1 = pt1.next if pt1 else headB
            pt2 = pt2.next if pt2 else headA
        return pt1