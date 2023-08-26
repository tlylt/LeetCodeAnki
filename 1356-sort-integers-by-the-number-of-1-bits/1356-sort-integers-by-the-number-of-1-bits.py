class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (self.count1(x), x))
    def count1(self, n):
        ans = 0
        while n > 0:
            ans += (n & 1)
            n >>= 1
        return ans