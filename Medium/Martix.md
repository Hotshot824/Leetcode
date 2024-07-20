### Martix

大部分的 Martix 都是用 array 來表示的，處理的時候要注意觀察 Martix 的變化跟 Array 的特性。

---

### [1380. Lucky Numbers in a Matrix]

因為這題中的每個數字都是 Unique，所以不會有重複的數字。
先找出每個 Row 的最小值，再找出每個 Column 的最大值，最後找出 Row 和 Column 的交集即可。

Time complexity O(n<sup>2</sup>), Space complexity O(n).

**Solution**
```go
func luckyNumbers(matrix [][]int) []int {
    minRow := make([]int, len(matrix))
    for i := range minRow {
        minRow[i] = int(^uint(0) >> 1)
    }
    maxCol := make([]int, len(matrix[0]))

    for i := range matrix {
        for j := range matrix[i] {
            if matrix[i][j] < minRow[i] {
                minRow[i] = matrix[i][j]
            }
            if matrix[i][j] > maxCol[j] {
                maxCol[j] = matrix[i][j]
            }
        }
    }

    var res []int
    for _, row := range minRow {
        for _, col := range maxCol {
            if row == col {
                res = append(res, row)
            }
        }
    }
    return res
}
```

[1380. Lucky Numbers in a Matrix]: https://leetcode.com/problems/lucky-numbers-in-a-matrix/