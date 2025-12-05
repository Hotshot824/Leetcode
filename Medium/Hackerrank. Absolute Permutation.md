---
Category: Math
Subcategory: Math
Title: Hackerrank. Absolute Permutation
Date: 2025-12-05
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Absolute Permutation]

[Hackerrank. Absolute Permutation]: https://www.hackerrank.com/challenges/absolute-permutation/problem

這題給了一種排列組合的方式，要求我們產生一個長度為 n 的排列組合 p，使得對於每一個位置 i (1 <= i <= n)，都有 |p[i] - i| = k。
如果沒有辦法產生這樣的排列組合，就回傳 -1。

-   `n = 4, k = 2`, `[3, 4, 1, 2]` is a valid absolute permutation since:
    -   `|3 - 1| = 2`
    -   `|4 - 2| = 2`
    -   `|1 - 3| = 2`
    -   `|2 - 4| = 2`
-   `n = 3, k = 0`, `[1, 2, 3]` is a valid absolute permutation since:
    -   `|1 - 1| = 0`
    -   `|2 - 2| = 0`
    -   `|3 - 3| = 0`

### Mathematical Solution
 
**1. K == 0**  
先考慮 k = 0 的情況，這種情況下，排列組合就是 1 到 n 的自然數列。

**2. K > 0**  
當 k > 0 時，要先思考這個 n 是否可能達成 Absolute Permutation，不是所有的 n 都能達成 Absolute Permutation。
以 `n = 4, k = 2` 為例，會發現其實每個 i 都有兩個選擇 `i + k` 或 `i - k`，例如:

-   `[1, 2, 3, 4]`
    -   首先我們會發現 arr[0] 只能是 3，如果是 -1 則會超出範圍。
    -   同時 arr[2] 也只能選擇 1，因為如果選擇 5 會超出範圍，這樣就形成一個 Pair (1, 3)
    -   接著 arr[1] 只能選擇 4，arr[3] 只能選擇 2，這樣就形成另一個 Pair (2, 4)
-   因此實際上這個 Absolute Permutation 可以被拆解成多個 Pair 組成，而每個 Pair 的長度是 2k。
    -   因為 arr[2+k] 的範圍內都只能去選擇 arr[0+k] ~ arr[k-1] 的值去做交換，如果 arr[2+k] 選擇做 +k 的動作會導致後面的數字找不到 Pair 可以交換。 
-   因此 n 必須要是 2k 的倍數才能形成完整的 Pair，否則就無法形成 Absolute Permutation。

這樣我們就能用 n % (2 * k) 來判斷是否能形成 Absolute Permutation，如果無法形成就直接回傳 -1。

-   以 `n = 8, k = 2` 為例，`[1, 2, 3, 4, 5, 6, 7, 8]` 可以被拆解成以下的 Pair:
    -   Pair 1: (1, 3), (2, 4)
    -   Pair 2: (5, 7), (6, 8)
-   一共兩個段落，每個段落長度都是 2k = 4，而每個段落都在做 arr[i] 與 arr[i+k] 的交換。

這樣 For loop 的寫法就會變成外層處理段落的移動，內層處理 arr[i] 與 arr[i+k] 的交換。
```
<!-- 1, 5 -->
for i := 0; i < n; i = i + 2*k {
    <!-- swap(1, 3), swap(2, 4) -->
    for j := i; j < i + k; j++ {
        res[j], res[j+k] = res[j+k], res[j]
    }
}
```

#### Algorithm

1. Initialize an array res with values from 1 to n.
2. If k is 0, return res as is.
3. If n is not divisible by 2*k, return [-1] as it's impossible to form an absolute permutation.
4. For each segment of size 2*k in res:
   - For the first k elements in the segment, swap each element with the element k positions ahead.
5. Return the modified res array.

Time Complexity O(n), Space Complexity O(n).

**Golang Solution:**
```go
/*
 * Complete the 'absolutePermutation' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 */
func absolutePermutation(n int32, k int32) []int32 {
    res := []int32{}
    
    if k != 0 && n % (2*k) != 0 {
        return []int32{-1}
    }
    
    for i := int32(1); i <= n; i++ {
        res = append(res, i)
    }
    
    if (k == 0) {
        return res
    }
    
    for i := int32(0); i < n; i = i + 2*k {
        for j := i; j < i + k; j++ {
            res[j], res[j+k] = res[j+k], res[j]
        }
    }
    
    return res
}
```

**C Solution:**
```c
int* absolutePermutation(int n, int k, int* result_count) {
    if (k != 0 && n % (2*k) != 0) {
        *result_count = 1;
        int* res = malloc(sizeof(int));
        res[0] = -1;
        return res;
    }
    
    *result_count = n;
    int* res = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        res[i] = i+1;
    }
    
    if (k == 0) {
        return res;
    }
    
    for (int i = 0; i < n; i = i + 2*k) {
        for (int j = i; j < i+k; j++) {
            int tmp = res[j];
            res[j] = res[j+k];
            res[j+k] = tmp;
        }
    }
    return res;
}
```