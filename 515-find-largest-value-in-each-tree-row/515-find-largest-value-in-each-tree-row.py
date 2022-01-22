# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        q = deque([root])
        while q:
            l = len(q)
            temp = float('-inf')
            for i in range(l):
                curr = q.popleft()
                temp = max(curr.val, temp)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(temp)
        return ans