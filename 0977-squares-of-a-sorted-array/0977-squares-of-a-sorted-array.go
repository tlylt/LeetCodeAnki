func sortedSquares(nums []int) []int {
    n:= len(nums)
    i, j, k := 0, n-1, n-1
    ans := make([]int, n)
    for i <= j {
        l, r := nums[i] * nums[i], nums[j] * nums[j]
        if l > r {
            ans[k] = l
            i++
        } else {
            ans[k] = r
            j--
        }
        k--
    }
    return ans
}