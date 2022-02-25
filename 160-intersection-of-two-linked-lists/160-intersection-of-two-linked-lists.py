# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l_a = self.findLength(headA)
        l_b = self.findLength(headB)
        while l_a > l_b:
            headA = headA.next
            l_a -= 1
        while l_b > l_a:
            headB = headB.next
            l_b -= 1
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
    def findLength(self, node):
        ans = 0
        while node:
            ans+=1
            node = node.next
        return ans