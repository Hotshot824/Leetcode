### Spiral Matrix

---

### [59. Spiral Matrix II]

String from a starting position `x`, `y`, how many circles are there in the matrix `loop = n/2`,
and then traverse the matrix in a clockwise direction. When a circle is traversed, the starting position `x-1`, `y-1`, `loop--`, `offset--`, 
if the traversal is completed when the `loop` is 0. Last to check if the matrix is odd, add the middle element.

[59. reference]

**Solution:**
```go
func generateMatrix(n int) [][]int {
	var result = make([][]int, n)
	for i := range result {
		result[i] = make([]int, n)
	}
	var x, y = 0, 0
	var loop, mid = n / 2, n / 2
	var count, offset = 1, 1

	for ; loop > 0; loop-- {
		var i, j = x, y

		for j = y; j < n-offset; j++ {
			result[x][j] = count
			count++
		}

		for i = x; i < n-offset; i++ {
			result[i][j] = count
			count++
		}

		for ; j > y; j-- {
			result[i][j] = count
			count++
		}

		for ; i > x; i-- {
			result[i][j] = count
			count++
		}

		x++
		y++
		offset++
	}

	if n%2 == 1 {
		result[mid][mid] = count
	}

	return result
}
```

[59. Spiral Matrix II]: https://leetcode.com/problems/spiral-matrix-ii/description/
[59. reference]: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.md

---

### [54. Spiral Matrix]

這題反而比 II 還要更複雜，因為這題有可能會出現長方形的矩陣:
1.	定義四個方向的移動 `{0, 1}, {1, 0}, {0, -1}, {-1, 0}`
2.	定義四個邊界 `top, bottom, left, right`
3.	如果再移動時超出邊界就依照移動的方向調整邊界，並轉換方向

![](/_image/Spiral_Matrix/1.jpg)

-	以上面的例子，如果最上方的 `1 -> 2 -> 3 -> 4` 移動完畢，代表 Top 將會緊縮
	-	接著移動 `8 -> 12` 此時 Right 將會緊縮
-	以此類推來做邊界的縮減

Time Complexity O(m*n).

**Solution:**
```go
var (
	directions = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
)

func spiralOrder(matrix [][]int) []int {
	m, n := len(matrix), len(matrix[0])
	length := m * n
	res := make([]int, length)

	d := 0
	x, y := 0, 0
    top, bottom, left, right := 0, m-1, 0, n-1
	for i := 0; i < length; i++ {
        res[i] = matrix[x][y]
		nx, ny := x+directions[d][0], y+directions[d][1]
        if nx < top || nx > bottom || ny < left || ny > right {
            switch d {
            case 0:
                top++
            case 1:
                right--
            case 2:
                bottom--
            case 3:
                left++
            }
            d = (d+1)%4
            nx, ny = x+directions[d][0], y+directions[d][1]
        }
        x, y = nx, ny
	}

	return res
}
```

[54. Spiral Matrix]: https://leetcode.com/problems/spiral-matrix/

---

### [2326. Spiral Matrix IV]

這題其實就是 II 的延伸，只是把題目改成了 Linked List 的形式，所以只要把 Linked List 轉換成矩陣的形式即可:
1.	定義四個方向的移動 `{0, 1}, {1, 0}, {0, -1}, {-1, 0}`
2.	定義四個邊界 `top, bottom, left, right`
3.	如果再移動時超出邊界就依照移動的方向調整邊界，並轉換方向
	-	`val = cur != nil ? cur.Val : -1`

Time Complexity O(m*n).

**Solution:**
```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
var (
	directions = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
)

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    res := make([][]int, m)
    for i := range res {
        res[i] = make([]int, n)
    }

    cur := head
    d, x, y := 0, 0, 0
    top, bottom, left, right := 0, m-1, 0, n-1
    for i := 0; i < m*n; i++ {
        val := -1
        if cur != nil {
            val = cur.Val
            cur = cur.Next
        }
        res[x][y] = val

        nx, ny := x+directions[d][0], y+directions[d][1]
        if nx < top || nx > bottom || ny < left || ny > right {
            switch d {
            case 0:
                top++
            case 1:
                right--
            case 2:
                bottom--
            case 3:
                left++
            }
            d = (d+1)%4
            nx, ny = x+directions[d][0], y+directions[d][1]
        }
        x, y = nx, ny
    }

    return res
}
```

[2326. Spiral Matrix IV]: https://leetcode.com/problems/spiral-matrix-iv/

---

### [885. Spiral Matrix III]

最直觀的想法是，這其實就是一個正方形的旋轉矩陣，我們來觀察一個正方形的旋轉矩陣的工作方式:

![](/_image/Martix/1.png)

我們會發現每次走過兩個方向後，步長會增加 1，如果用這種方式來尋找所有旋轉矩陣的 Item，
就只要檢查新的 x, y 是否超出邊界就好，如果沒有就加入 Res。

Time complexity O(n*m), Space complexity O(n*m).

**Solution:**
```go
func spiralMatrixIII(rows int, cols int, rStart int, cStart int) [][]int {
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	result := [][]int{{rStart, cStart}}
	steps := 1
	x, y := rStart, cStart

	for len(result) < rows*cols {
		for i := 0; i < 4; i++ {
			for j := 0; j < steps; j++ {
				x += directions[i][0]
				y += directions[i][1]
				if x >= 0 && x < rows && y >= 0 && y < cols {
					result = append(result, []int{x, y})
				}
			}
			if i%2 == 1 {
				steps++
			}
		}
	}

	return result
}
```

[885. Spiral Matrix III]: https://leetcode.com/problems/spiral-matrix-iii