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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque([root])
        while q:
            l = len(q)
            prev = None
            for i in range(l):
                c = q.popleft()
                if not prev:
                    prev = c
                else:
                    prev.next = c
                if c.left:
                    q.append(c.left)
                if c.right:
                    q.append(c.right)
                prev = c
        return root
                    