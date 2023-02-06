class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        ref = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ref[0 - (nums1[i] + nums2[j])] = ref.get((0-(nums1[i] + nums2[j])), 0) + 1
        for x in range(len(nums3)):
            for y in range(len(nums4)):
                ans += ref.get(nums3[x] + nums4[y], 0)
        return ans