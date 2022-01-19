import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        ans = []
        for i in nums:
            h[i] = h.get(i,0) + 1
        for ke, val in h.items():
            heapq.heappush(ans, (val, ke))
        result =[]
        for i in range(len(ans)-k):
            heapq.heappop(ans)
        for j in range(k):
            result.append(heapq.heappop(ans)[1])
        return result