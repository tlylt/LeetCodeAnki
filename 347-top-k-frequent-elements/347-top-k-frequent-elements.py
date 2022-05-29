import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1
        ref = []
        for ke, va in h.items():
            heapq.heappush(ref, (va, ke))
        for i in range(len(ref) - k):
            heapq.heappop(ref)
        ans = []
        for i in ref:
            ans.append(i[1])
        return ans