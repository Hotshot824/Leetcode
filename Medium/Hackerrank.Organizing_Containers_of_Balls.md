---
Category: Array
Subcategory: Sort
Title: Hackerrank. Organizing Containers of Balls
Date: 2025-09-15
Difficulty: Medium
Tag: Math, Hash
Status: Accepted
---

### [Hackerrank. Organizing Containers of Balls]

[Hackerrank. Organizing Containers of Balls]: https://www.hackerrank.com/challenges/organizing-containers-of-balls

> 這題我要先吐槽一下題目敘述跟 Sample Input/Output 給的資訊，不是用 C 的話根本看不懂 Sample Input/Output 是什麼意思，
提前給了兩個 imput 是用來說明 Array 結構的，但在其他語言中也跑出這兩個 Input，會讓人搞不清楚這兩個 Input 是什麼意思。

這題是給定一個 n x n 的 2D Array，Array[i][j] 代表第 i 個 Container 裡面有多少個 j 類型的 Ball，
每個 Container 可以裝任意數量的 Ball，然後我們可以任意交換兩個 Container 裡面的 Ball，
問我們能不能把這些 Ball 交換成每個 Container 裡面只裝一種類型的 Ball。

---

### Sort

簡單來說這題就是說，我們有 n 個 Container 和 n 種 Ball 類型。

-   一開始每個 Container 都裝滿的，但是裡面不一定是同一種類型的 Ball
    -   這裡要注意每個 Container 容量可能不一樣
-   最終目的是能否讓每個 Container 裡面只裝一種類型的 Ball
    -   只要回答 "Possible" 或 "Impossible" 就好
-   並且同一種 Ball 類型只能放在同一個 Container 裡面

這樣就很簡單了，把 Row Sum 和 Column Sum 都算出來，然後把兩個 Sum 排序之後比較是否相等。

如果不相等就代表某個 Container 的容量不夠放某種類型的 Ball 或者某種類型的 Ball 太多放不進任何一個 Container。

Time Complexity O(N^2), Space Complexity O(N).

**Go Solution:**
```go
/*
 * Complete the 'organizingContainers' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts 2D_INTEGER_ARRAY container as parameter.
 */

func organizingContainers(container [][]int32) string {
    balls := make([]int32, len(container))
    recontainers := make([]int32, len(container))
    
    for i, c := range container {
        for j, b := range c {
            balls[j] += b
            recontainers[i] += b
        }
    }
    
    sortInt32(balls)
    sortInt32(recontainers)
    
    for i := range balls {
        if balls[i] != recontainers[i] {
            return "Impossible"
        }
    }
    return "Possible"
}
```