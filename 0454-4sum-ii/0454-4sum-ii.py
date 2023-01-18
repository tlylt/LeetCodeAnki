class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ref = {}
        ans = 0
        for i in nums1:
            for j in nums2:
                ref[i+j] = ref.get(i+j, 0) + 1
        for x in nums3:
            for y in nums4:
                if (0-x-y) in ref:
                    ans += ref[0-x-y]
        return ans