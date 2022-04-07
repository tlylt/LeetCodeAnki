import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1
        ans = []
        for ke, va in h.items():
            heappush(ans, (va, ke))
        result = []
        for i in range(len(ans)-k):
            heappop(ans)
        for i in range(k):
            result.append(heappop(ans)[1])
        return result