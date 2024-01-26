func removeElement(nums []int, val int) int {
    pt := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != val {
            nums[pt] = nums[i]
            pt++            
        }
    }
    return pt
}