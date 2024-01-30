class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1
