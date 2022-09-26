import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = {}
        for i in range(len(nums)):
            ref[nums[i]] = ref.get(nums[i], 0) + 1
        ans = []
        for ke, va in ref.items():
            heapq.heappush(ans, (va, ke))
            if len(ans) > k:
                heapq.heappop(ans)
        result = []
        for i in range(k):
            result.append(heapq.heappop(ans)[1])
        return result