import heapq # min heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums)+1)]
        ref = {}
        for i in nums:
            ref[i] = ref.get(i, 0) + 1
        for ke,va in ref.items():
            ans[va].append(ke)
        result = []
        for j in range(len(ans)-1, 0, -1):
            if k > 0 and ans[j] != []:
                for z in ans[j]:
                    result.append(z)
                    k -= 1
                    if k == 0:
                        break
        return result