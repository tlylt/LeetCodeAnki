# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(None, head)
    def helper(self, prev, node):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return self.helper(node, temp)