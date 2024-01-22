func commonChars(words []string) []string {
    if len(words) == 0 {
        return []string{}
    }
    ref := [26]int{}
    for _, c := range words[0] {
        ref[c - 'a']++
    }
    
    for j := 1; j < len(words); j++ {
        ref2 := [26]int{}
        for _, k := range words[j] {
            ref2[k-'a']++
        }
        for x:=0; x < 26; x++ {
            if ref[x] > ref2[x] {
                ref[x] = ref2[x]
            }
        }
    }
    
    var ans []string
    for y := 0; y < 26; y++ {
        for ref[y] > 0 {
            ans = append(ans, string('a' + y))
            ref[y]--
        }
    }
    return ans
}