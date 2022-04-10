"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        s = deque()
        if not root:
            return
        s.append(root)
        while s:
            l = len(s)
            prev = None
            for i in range(l):
                curr = s.popleft()
                if prev:
                    prev.next = curr
                prev = curr
                if curr.left:
                    s.append(curr.left)
                if curr.right:
                    s.append(curr.right)
        return root