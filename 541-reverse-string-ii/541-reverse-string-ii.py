class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(s), 2*k):
            arr[i:i+k] = arr[i:i+k][::-1]
        return "".join(arr)