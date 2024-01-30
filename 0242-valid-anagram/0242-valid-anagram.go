func isAnagram(s string, t string) bool {
    ref := [26]int{}
    for _, r := range s {
        ref[r - rune('a')]++
    }
    for _, r := range t {
        ref[r - rune('a')]--
    }
    
    return ref == [26]int{}
}