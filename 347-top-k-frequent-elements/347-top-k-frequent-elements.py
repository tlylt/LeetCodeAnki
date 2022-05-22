import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = h.get(nums[i], 0) + 1
        buckets = [[] for i in range(len(nums)+1)]
        for ke, va in h.items():
            buckets[va].append(ke)
        ans = []
        curr = len(nums)
        while k:
            while len(buckets[curr]) == 0:
                curr -= 1
            for i in range(len(buckets[curr])):
                ans.append(buckets[curr][i])
                k -= 1
            curr -= 1
        return ans
            
            