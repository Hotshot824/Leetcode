---
Category: String
Subcategory: String
Title: Hackerrank. Repeated String
Date: 2025-09-15
Difficulty: Easy
Status: Accepted
---

### [Hackerrank. Repeated String]

[Hackerrank. Repeated String]: https://www.hackerrank.com/challenges/repeated-string/problem

很簡單的題目，就是給定一個字串 s，然後重複這個字串直到長度達到 n，然後問在這個長度為 n 的字串中有多少個 'a'。

---

### Count

做兩個步驟:

1. 第一個步計算完整的字串 s 裡面有多少個 'a'，然後乘上 n / len(s)
2. 第二個步計算剩下的字串 s 裡面有多少個 'a'，然後加上去

Time Complexity O(N), Space Complexity O(1).

**Golang Solution:**
```go
func repeatedString(s string, n int64) int64 {
    count := 0
    for _, c := range s {
        if c == 'a' {
            count++
        }
    }

    res := int64(count) * (n / int64(len(s)))

    for i := 0; i < int(n)%len(s); i++ {
        if s[i] == 'a' {
            res++
        }
    }
    return res
}
```