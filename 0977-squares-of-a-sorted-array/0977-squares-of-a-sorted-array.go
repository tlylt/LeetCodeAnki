func sortedSquares(nums []int) []int {
    ans := make([]int, len(nums))
    pt := len(nums) - 1
    l, r := 0, len(nums) - 1
    for l <= r {
        a, b := nums[l] * nums[l], nums[r] * nums[r]
        if a > b {
            ans[pt] = a
            l++
        } else {
            ans[pt] = b
            r--
        }
        pt--
    }
    return ans
}