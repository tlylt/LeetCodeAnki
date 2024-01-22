func intersection(nums1 []int, nums2 []int) []int {
    set := make(map[int]struct{}, 0)
    ans := make([]int, 0)
    for _, v := range nums1 {
        if _, ok := set[v]; !ok {
            set[v] = struct{}{}
        }
    }
    for _, v := range nums2 {
        if _, ok := set[v]; ok {
            ans = append(ans, v)
            delete(set, v)
        }
    }
    return ans
}