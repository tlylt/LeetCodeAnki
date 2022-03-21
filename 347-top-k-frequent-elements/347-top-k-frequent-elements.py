import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1
        buckets = [[] for i in range(len(nums))]
        for ke, va in h.items():
            buckets[va-1].append(ke)
        ans = []
        for ls in buckets[::-1]:
            for i in ls:
                if k == 0:
                    return ans
                ans.append(i)
                k -= 1
        return ans
            