"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            l = len(q)
            temp = []
            for i in range(l):
                c = q.popleft()
                temp.append(c.val)
                for ch in c.children:
                    q.append(ch)
            ans.append(temp)
        return ans