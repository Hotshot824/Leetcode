---
Category: Array
Subcategory: Matrix
Title: Forming a Magic Square
Date: 2025-09-13
Difficulty: Medium
Status: Accepted
---

### [Forming a Magic Square]

[Forming a Magic Square]: https://www.hackerrank.com/challenges/magic-square-forming/problem

Hackerrank 的題目，給一個 3*3 矩陣，找出該矩陣變為 Magic Square 所需的最小 cost。
-   Magic Square 的定義是每一行、每一列、兩條對角線的和都相等
-   Cost 則是原本矩陣的數字變成 Magic Square 的數字所需的差值絕對值總和

---

### Backtracking

算差值的部分很簡單，主要是要找出所有可能的 Magic Square，
我不信這邊都是 Hardcoded 的解法，所以我用 Backtracking 找出所有可能的 Magic Square。

1. Define Lines 就是所有行、列、對角線
    -   用一個陣列來存每一條線的三個位置
2. Magic Square 的中間數字必然是 5
    -   所以下去 Backtracking 的時候就先把 5 放在中間
3. Backtracking
    -   isMagicSquare 判斷目前的陣列是不是可能的 Magic Square
        -   如果有任何一條線的和大於 15 就不可能是 Magic Square
    -   每個位置都嘗試放入 1-9 的數字
    -   如果所有數字都放完了，並且是 Magic Square 就把它存起來
4. 最後把所有的 Magic Square 都算一次差值，取最小值回傳

Time Complexity O(1), Space Complexity O(1).

**Golang Solution:**
```go
func formingMagicSquare(s [][]int32) int32 {
    new_s := make([]int32, 9)
    idx := 0
    for _, r := range s {
        for _, num := range r {
            new_s[idx] = num
            idx++
        }
    }

    findMagicSquare()

    res := int32(1<<31 - 1)
    for _, ms := range magicSquare {
        var temp int32 = 0
        for i := range ms {
            temp += abs(ms[i] - new_s[i])
        }
        if temp < res {
            res = temp
        }
    }
    return res
}

func abs(a int32) int32 {
    if a > 0 {
        return a
    }
    return -a
}

var lines = [8][3]int32{
    {0, 1, 2},
    {3, 4, 5},
    {6, 7, 8},
    {0, 3, 6},
    {1, 4, 7},
    {2, 5, 8},
    {0, 4, 8},
    {6, 4, 2},
}

var nums = []int32{1, 2, 3, 4, 6, 7, 8, 9}

var pos = []int32{0, 1, 2, 3, 5, 6, 7, 8}

var magicSquare = [][]int32{}

func findMagicSquare() {
    magicSquare = [][]int32{}
    temp := []int32{0, 0, 0, 0, 5, 0, 0, 0, 0}
    backtracking(temp, 0)
}

func backtracking(square []int32, nidx int) {
    if !isMagicSquare(square) {
        return
    }
    
    if nidx == len(nums) {
        cp := make([]int32, len(square))
        copy(cp, square)
        magicSquare = append(magicSquare, cp)
        return
    }

    for _, p := range pos {
        if square[p] != 0 {
            continue
        }
        square[p] = nums[nidx]
        backtracking(square, nidx+1)
        square[p] = 0
    }
}

func isMagicSquare(square []int32) bool {
    for _, line := range lines {
        var sum int32 = 0
        for _, p := range line {
            sum += square[p]
        }
        if sum > 15 {
            return false
        }
    }
    return true
}
```