func intersection(nums1 []int, nums2 []int) []int {
    count1 := make([]int, 1001, 1001)
    count2 := make([]int, 1001, 1001)
    res := make([]int, 0)
    for _, v := range nums1 {
        count1[v] = 1
    }
    for _, v := range nums2 {
        count2[v] = 1
    }
    for i := 0; i <= 1000; i++ {
        if count1[i] + count2[i] == 2 {
            res = append(res, i)
        }
    }
    return res
}