import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        for i in range(len(nums)+1):
            bucket.append([])
        h = {}
        for j in nums:
            h[j] = h.get(j, 0) + 1
        for ke,va in h.items():
            bucket[va].append(ke)
        ans = []
        while k:
            if not bucket:
                return ans
            if bucket[-1]:
                for i in bucket[-1]:
                    ans.append(i)
                    k-=1
            bucket.pop()
        return ans