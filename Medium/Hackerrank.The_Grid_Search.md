---
Category: Array
Subcategory: Matrix
Title: Hackerrank. The Grid Search
Date: 2025-12-04
Difficulty: Medium
Tag: Array
Status: Accepted
---

### [Hackerrank. The Grid Search]

[Hackerrank. The Grid Search]: https://www.hackerrank.com/challenges/the-grid-search/problem

這個問題給了兩個 Matrix，分別是 G 和 P，然後要我們判斷 P 是否有出現在 G 裡面。

雖然問題描述給了很多其他的條件，但其實最主要的就是要我們判斷 P 這個 Matrix 是否有出現在 G 裡面。
要吐槽一下 Hackerrank 的 Golang main 裡面寫錯了，Golang 很雞婆的每個宣告的變數都要用到，不然會編譯錯誤，
但 Hackerrank 的 main 裡面有宣告一些變數卻沒有用到，導致無法編譯通過，因此要修改一下 main 裡面的程式碼才能通過。

---

### Brute Force Solution

如果在面試場合遇到這題，最好就是寫 Brute Force，其他演算法應該很難在當下想到跟寫出來。

1. Scan G Matrix's each element as a potential starting point.
2. For each starting point, check if P Matrix matches G Matrix from that point.
3. If a match is found, return "YES". If no matches are found after scanning all starting points, return "NO".

Time Complexity O(N*M*P*Q), N and M are dimensions of G, P and Q are dimensions of P.
Space Complexity O(1).

**Golang Solution:**
```go
/*
 * Complete the 'gridSearch' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING_ARRAY G
 *  2. STRING_ARRAY P
 */

func gridSearch(G []string, P []string) string {
    
    for i := 0; i < len(G); i++ {
        for j := 0; j < len(G[i]); j++ {
            if G[i][j] != P[0][0] {
                continue
            }
            if checkPattern(G, P, i, j) {
                return "YES"
            }
        }
    }
    
    return "NO"
}

func checkPattern(G []string, P[]string, x, y int) bool {
    for i := 0; i < len(P); i++ {
        if x >= len(G) {
            return false
        }
        tmp := y
        for j := 0; j < len(P[0]); j++ {
            if tmp >= len(G[x]) {
                return false
            }
            if P[i][j] != G[x][tmp] {
                return false
            }
            tmp++
        }
        x++
    }
    return true
}
```

**C Solution:**
-   Do some purning to avoid unnecessary checks.
```c
bool checkPattern(int G_count, char** G, int P_count, char** P, int x, int y) {

    for (int i = 0; i < P_count; i++) {

        if (x >= G_count) return false;
        
        int tmp = y;
        int rowLenG = strlen(G[x]);
        int rowLenP = strlen(P[i]);

        if (tmp + rowLenP > rowLenG) return false;

        for (int j = 0; j < rowLenP; j++) {
            if (G[x][tmp] != P[i][j]) return false;
            tmp++;
        }
        x++;
    }

    return true;
}

char* gridSearch(int G_count, char** G, int P_count, char** P) {

    for (int i = 0; i < G_count; i++) {
        int width = strlen(G[i]);
        if (i + P_count > G_count)
            break;
        for (int j = 0; j < width; j++) {
            if (G[i][j] != P[0][0])
                continue;
            if (j + strlen(P[0]) > width)
                continue;
            if (checkPattern(G_count, G, P_count, P, i, j))
                return "YES";
        }
    }
    return "NO";
}
```

### KMP Solution

這邊簡單講 KMP 的思路，把 Row 拆開當成字串，這樣就可以用 KMP 來做字串搜尋。
在每一列找 P 在 G 裡面出現的位置，然後記錄下來，接著檢查這些位置是否有連續出現 P 的所有列。

1. Preprocess each row of P to create the KMP "longest prefix-suffix" (LPS) array.
2. For each row in G, use the KMP algorithm to find all occurrences of the first row of P.
3. For each occurrence found, check if the subsequent rows of P match the corresponding rows in G.
4. If a complete match is found, return "YES". If no matches are found after scanning all rows, return "NO".

Time Complexity O(N*M + P*Q), Space Complexity O(P).