class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        h = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                h[0-nums1[i]-nums2[j]] = h.get(0-nums1[i]-nums2[j], 0) + 1
        ans = 0
        for x in range(len(nums3)):
            for y in range(len(nums4)):
                if nums3[x]+nums4[y] in h:
                    ans += h[nums3[x]+nums4[y]]
        return ans