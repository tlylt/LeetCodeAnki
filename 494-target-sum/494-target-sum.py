        # sumPos + sumNeg = total
        # sumPos - (sumNeg) = target
        # sumNeg = total - sumPos
        # sumPos - (total - sumPos) = target
        # sumPos = (target + total) / 2
        # sumPos = bagSize
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        bagSize = (total + target) // 2
        if (total + target) % 2 == 1:
            return 0
        if abs(target) > total:
            return 0
        dp = [0] * (bagSize + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagSize, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        return dp[bagSize]