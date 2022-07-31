import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for i in nums:
            ref[i] = ref.get(i, 0) + 1
        h = []
        for ke, va in ref.items():
            heapq.heappush(h, (va, ke))
        ans = []
        for i in range(len(h)-k):
            heapq.heappop(h)
        for j in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans