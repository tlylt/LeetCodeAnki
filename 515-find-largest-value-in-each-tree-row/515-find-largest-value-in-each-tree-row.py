# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        d = deque([root])
        while d:
            temp = float('-inf')
            l = len(d)
            for i in range(l):
                curr = d.popleft()
                temp = max(temp, curr.val)
                if curr.left:
                    d.append(curr.left)
                if curr.right:
                    d.append(curr.right)
            ans.append(temp)
        return ans