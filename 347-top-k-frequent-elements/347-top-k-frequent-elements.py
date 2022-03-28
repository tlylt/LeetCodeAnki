import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        ans = []
        for ke, va in h.items():
            heappush(ans, (va, ke))
        for i in range(len(ans)-k):
            heappop(ans)
        result = []
        for i in ans:
            result.append(i[1])
        return result