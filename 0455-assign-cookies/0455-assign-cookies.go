func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)
    ans := 0
    pt := len(s) - 1 
    for idx := len(g) - 1; idx >= 0; idx-- {
        if pt >= 0 && s[pt] >= g[idx] {
            ans++
            pt--
        }
    }
    return ans
}