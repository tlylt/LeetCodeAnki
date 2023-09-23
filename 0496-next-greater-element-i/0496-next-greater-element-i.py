class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        ref = {}
        for i in range(len(nums1)):
            ref[nums1[i]] = i
        
        stack = [0]
        for j in range(1, len(nums2)):
            curr = nums2[j]
            while stack and curr > nums2[stack[-1]]:
                top = stack.pop()
                if nums2[top] in ref:
                    idx = ref[nums2[top]]
                    ans[idx] = curr
            stack.append(j)
        return ans