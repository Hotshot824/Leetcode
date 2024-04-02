### [205. Isomorphic Strings]

判斷兩個 String pattern 是否相同，最簡單的方式就是建立兩個 Hash，分別記錄 i 上次出現的位置，
如果 pattern 不同，那麼 i 上次出現的位置也應該不同，否則就是相同的 pattern。
-   使用位置而不是計數，是因為計數的話，無法判斷 "aabbb" 跟 "bbaab" 這種情況。

Time Complexity O(n).

**Solution:**
```go
func isIsomorphic(s string, t string) bool {
    hash1, hash2 := map[byte]int{}, map[byte]int{}
    for i := range s {
        if hash1[s[i]] != hash2[t[i]] {
            return false
        } else {
            hash1[s[i]] = i+1
            hash2[t[i]] = i+1
        }
    }
    return true
}
```

[205. Isomorphic Strings]: https://leetcode.com/problems/isomorphic-strings

---

### [290. Word Pattern]

基本上的想法跟上一題一樣，只是這次是比對 pattern 跟字串的關係，所以要多做一些處理，並且這題的 pattern 跟 s 並不一定是一對一的關係，所以要比較長度。

```go
func wordPattern(pattern string, s string) bool {
    s_slice := strings.Split(s, " ")
    if len(pattern) != len(s_slice) {
        return false
    }
    hash1, hash2 := map[byte]int{}, map[string]int{}
    for i := range s_slice {
        if hash1[pattern[i]] != hash2[s_slice[i]] {
            return false
        } else {
            hash1[pattern[i]] = i+1
            hash2[s_slice[i]] = i+1
        }
    }
    return true
}
```

[290. Word Pattern]: https://leetcode.com/problems/word-pattern/description/