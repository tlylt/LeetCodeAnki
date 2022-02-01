import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1
        buckets = [[] for i in range(len(nums)+1)]
        for ke, va in h.items():
            buckets[va].append(ke)
        flat = []
        for ls in buckets[::-1]:
            for i in ls:
                flat.append(i)
        return flat[:k]