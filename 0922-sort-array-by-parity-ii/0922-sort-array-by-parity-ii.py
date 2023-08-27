class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(nums), 2):
            if nums[even] % 2 == 1:
                while nums[odd] % 2 == 1:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums