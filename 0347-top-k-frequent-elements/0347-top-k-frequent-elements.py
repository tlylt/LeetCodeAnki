import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for i in nums:
            ref[i] = ref.get(i, 0) + 1
        heap = []
        for ke, va in ref.items():
            heapq.heappush(heap, (va, ke))
        ans = []
        for i in range(len(heap) - k):
            heapq.heappop(heap)
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans