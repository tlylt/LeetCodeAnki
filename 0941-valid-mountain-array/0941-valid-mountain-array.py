class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = 0
        r = len(arr) - 1
        while l < len(arr) - 1 and arr[l] < arr[l+1]:
            l += 1
        while r > 1 and arr[r] < arr[r-1]:
            r -= 1
        return l == r and l != 0 and r != len(arr) - 1
        