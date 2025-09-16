---
Category: String
Subcategory: String
Title: Hackerrank. Encryption
Date: 2025-09-16
Difficulty: Medium
Tag: String, Encryption
Status: Accepted
---

### [Hackerrank. Encryption]

[Hackerrank. Encryption]: https://www.hackerrank.com/challenges/encryption/problem

這題會給定一個字串，要求對該字串進行加密，規則如下:

1. 首先移除字串中的空格
2. 計算字串長度 L，找出兩個整數 rows 和 columns，使得整個字串可以塞入 rows * columns 的矩陣中，且滿足以下條件:
   - `sqrt(L) <= rows <= columns <= ceil(sqrt(L))`
3. 將字串按行填入矩陣中，然後按列讀取矩陣，並在每個列之間加入空格，形成加密後的字串

Example:

```
Input: "have a nice day"

Row = 3, Column = 4

Square:
have
anic
eday

Output: "hae and via ecy"
```

> 注意輸出是按照 Col, Row 的順序來讀取的

--- 

### Implementation

加密題目就只能照著規則一步步來，照著題目的規則來計算即可。

> 移除空字串通常有 lib 可以用，忘了就只能自己做了

> 要記一下 ceil 的用法，忘了的話就只能暴力解了，這個 function 平時比較少用

Time Complexity O(N), Space Complexity O(N).

**CPP Solution:**
```cpp
/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

string encryption(string s) {
    int size = s.size();
    string erase_space = "";
    for (int i = 0; i < size; i++) {
        if (s[i] == ' ') {
            continue;
        }
        erase_space += s[i];
    }
    
    size = erase_space.size();
    
    int col = (int)ceil(sqrt(size));
    
    string res = "";
    for (int c = 0; c < col; c++) {
        for (int i = c; i < size; i += col) {
            res += erase_space[i];
        }
        if (c < col - 1) res += " ";
    }
    return res;
}
```

**Golang Solution:**
```go
/*
 * Complete the 'encryption' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func encryption(s string) string {
    var b strings.Builder
    for _, r := range s {
        if r != ' ' {
            b.WriteRune(r)
        }
    }
    erase_spaces := b.String();
    
    col := int(math.Ceil(math.Sqrt(float64(len(s)))))
    
    b.Reset()
    
    for c := 0; c < col; c++ {
        for i := c; i < len(erase_spaces); i += col {
            b.WriteByte(erase_spaces[i])
        }
        if (c < col - 1) {
            b.WriteByte(' ')
        }
    }
    
    return b.String()
}
```