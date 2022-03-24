import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1
        for ke, va in h.items():
            heappush(ans, (va, ke))
        for i in range(len(ans)-k):
            heappop(ans)
        result = []
        for i in range(k):
            result.append(heappop(ans)[1])
        return result