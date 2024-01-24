func dailyTemperatures(temperatures []int) []int {
    ans := make([]int, len(temperatures))
    stack := []int{}
    for i, v := range temperatures {
        for len(stack) != 0 && v > temperatures[stack[len(stack)-1]] {
            top := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            
            ans[top] = i - top
        }
        stack = append(stack, i)
    }
    return ans
}