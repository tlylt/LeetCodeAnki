import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        ans = []
        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1
        for ke, va in h.items():
            heapq.heappush(ans, (va, ke))
        for i in range(len(ans)-k):
            heapq.heappop(ans)
        result = []
        for j in range(k):
            result.append(heapq.heappop(ans)[1])
        return result