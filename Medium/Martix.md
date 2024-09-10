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

---

### [1605. Find Valid Matrix Given Row and Column Sums]

這裡可以用 Greedy 的方式來解決，因為是每個 Row 和 Column 的和，這樣可以用逐一分配的方式來解決。
1.  比較 rowSum[i] 和 colSum[j] 的最小值，取最小值放入 res[i][j]
    -   並且 rowSum[i] 和 colSum[j] 要扣除已經分配掉的值
2.  重複上述步驟直到 rowSum 和 colSum 都為 0

**Example:**
1.  比較 rowSum[i] 和 colSum[j] 的最小值，取最小值放入 res[i][j]。
    -   rowSum = [5,7,10], colSum = [8,6,8]
    ```
    rowSum[0] = 5, colSum[0] = 8, min(5, 8) = 5

    5 0 0
    0 0 0,  Remaining: [0,7,10], [3,6,8]
    0 0 0

    rowSum[0] = 0, colSum[1] = 6, min(0, 6) = 0

    5 0 0
    0 0 0,  Remaining: [0,7,10], [3,6,8]
    0 0 0
    ```
    -   這個步驟代表的是 res[0] 的所有條件都已經滿足，同時 colSum[0] = 3 也已經扣除
2.  重複上述步驟
    -   rowSum = [0,7,10], colSum = [5,6,8]
    ```
    rowSum[1] = 7, colSum[0] = 3, min(7, 3) = 3

    5 0 0
    3 0 0,  Remaining: [0,4,10], [0,1,8]
    0 0 0
    ```
    -   這裡會發現 rowSum[0], colSum[0] 都已經為 0，代表這兩個方向的數字都已經滿足。
3.  重複上述步驟直到結束。

Time complexity O(n*m), Space complexity O(n*m).

**Solution:**
```go
func restoreMatrix(rowSum []int, colSum []int) [][]int {
    res := make([][]int, len(rowSum))
    for i := range res {
        res[i] = make([]int, len(colSum))
    }

    for i := range rowSum {
        for j := range colSum {
            res[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
        }
    }
    return res
}
```

[1605. Find Valid Matrix Given Row and Column Sums]: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

---

### [48. Rotate Image]

這題如果再不使用同個 Address 或者額外的 Space 的情況下，就需要計算出每次旋轉的交換位置。
每次交換就一次交換完成，所以只需要交換 n/2 次即可。

-   以下為例每一步就完成所有的交換，所以只需要交換 n/2 次即可
```
1 2 3    7 2 1
4 5 6 -> 4 5 6
7 8 9    9 8 3
```

Time Complexity O(n<sup>2</sup>), Space Complexity O(1).

**Solution:**
```go
func rotate(matrix [][]int)  {
    m, n := len(matrix), len(matrix[0])
    top, bottom, left, right := 0, m-1, 0, n-1

    for bottom > top {
        for i := 0; i < right-left; i++ {
            a := matrix[top][left+i]
            b := matrix[top+i][right]
            c := matrix[bottom][right-i]
            d := matrix[bottom-i][left]
            matrix[top][left+i] = d
            matrix[top+i][right] = a
            matrix[bottom][right-i] = b
            matrix[bottom-i][left] = c
        }
        top++
        bottom--
        left++
        right--
    }
}
```

[48. Rotate Image]: https://leetcode.com/problems/rotate-image/