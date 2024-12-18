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

### [2490. Circular Sentence]

這裡用一個簡單的方式來解決這個問題，就是判斷第一個字元跟最後一個字元是否相同，如果不同就直接回傳 false，
接著就是判斷每個 White Space 前後的字元是否相同，如果不同就回傳 false。

Time Complexity O(n).

**Solution:**
```go
func isCircularSentence(sentence string) bool {
    size := len(sentence)
    if sentence[0] != sentence[size-1] {
        return false
    }
    for i, n := range sentence {
        if n != ' ' {
            continue
        }
        if sentence[i-1] != sentence[i+1] {
            return false
        }
    }
    return true
}
```

[2490. Circular Sentence]: https://leetcode.com/problems/circular-sentence

---

### [2185. Counting Words With a Given Prefix]

-   很簡單的做法，直接對每個字串做比對即可，如果有符合的就 Res++

Time Complexity O(n), Space Complexity O(1).

**Solution**
```go
func prefixCount(words []string, pref string) int {
    res := 0
    tar := len(pref)
    for _, n := range words {
        if len(n) >= tar && n[:tar] == pref {
            res++
        }
    }
    return res
}
```

[2185. Counting Words With a Given Prefix]: https://leetcode.com/problems/counting-words-with-a-given-prefix

---

### [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence]

-   這題的解法就是對每個字串做比對，如果有符合的就回傳 index
-   盡量不使用 Split 來處理，只使用 Index 來處理

Time Complexity O(n), Space Complexity O(1).

**Solution**
```go
func isPrefixOfWord(sentence string, searchWord string) int {
    n := len(sentence)
    tn := len(searchWord)
    start, end := 0, 0
    wordIndex := 1

    for end <= n {
        if end == n || sentence[end] == ' ' {
            if end-start >= tn && sentence[start:start+tn] == searchWord { 
                return wordIndex
            }
            wordIndex++
            start = end + 1
        }
        end++
    }

    return -1
}

```

[1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence]: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence