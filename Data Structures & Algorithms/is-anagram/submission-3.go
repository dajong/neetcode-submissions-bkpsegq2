func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sMap, tMap := make(map[rune]int), make(map[rune]int)

    for i, c := range s{
        sMap[c]++
        tMap[rune(t[i])]++
    }

    for k, v := range sMap {
        if tMap[k] != v {
            return false
        }
    }

    return true
}
