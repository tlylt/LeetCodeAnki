        # sumPos + sumNeg = total
        # sumPos - (sumNeg) = target
        # sumNeg = total - sumPos
        # sumPos - (total - sumPos) = target
        # sumPos = (target + total) / 2
        # sumPos = bagSize
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2:
            return 0
        if abs(target) > total:
            return 0
        bagSize = (total + target) // 2
        dp = [0] * (bagSize+1)
        dp[0] = 1
        for i in nums:
            for j in range(bagSize, -1, -1):
                if j >= i:
                    dp[j] += dp[j-i]
        return dp[bagSize]