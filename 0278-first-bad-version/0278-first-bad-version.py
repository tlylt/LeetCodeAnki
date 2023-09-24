# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.merge(0, n+1)

    def merge(self, l, r):
        if r <= l:
            return l
        mid = l + (r-l) // 2
        if isBadVersion(mid):
            return self.merge(l, mid)
        else:
            return self.merge(mid + 1, r)