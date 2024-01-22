func commonChars(words []string) []string {
    ref := make([]int, 26)
    for _, char := range words[0] {
        ref[char-'a']++
    }
    for i := 1; i < len(words); i++ {
        ref2 := make([]int, 26)
        w := words[i]
        for _, char := range w {
            ref2[char-'a']++
        }
        for idx, val := range ref {
            if val > ref2[idx] {
                ref[idx] = ref2[idx]
            }
        }
    }
    totalElements := 0
    for _, val := range ref {
        totalElements += val
    }

    ans := make([]string, 0, totalElements)
    for idx, val := range ref {
        for val > 0 {
            ans = append(ans, string('a' + idx))
            val--
        }
    }
    return ans
}