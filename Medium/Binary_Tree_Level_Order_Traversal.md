### Binary Tree Level Order Traversal

[Reference]  

Level order 的歷遍方式是逐層的遍歷，核心思想是使用 Queue 來實現，因為 Queue 是先進先出的特性，
所以可以使用這個特性來設計遍歷函數。
  
**Golang TreeNode Struct**
```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
```

---

### [102. Binary Tree Level Order Traversal]

這裡有兩個主要的步驟需要注意：
1. 將當前層的 Node 的 SubNode 加入到 Queue
2. 將當前層的所有 Node Pop，並將值加入到 Res

**Iteration Solution:**
```go
func levelOrder(root *TreeNode) [][]int {
	var result [][]int
	var queue []*TreeNode
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size int = len(queue)
		var level []int
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			level = append(level, cur.Val)
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
		result = append(result, level)
	}
	return result
}
```

**Recursion Solution:**
```go
func levelOrder(root *TreeNode) [][]int {
	var result [][]int
	order(root, &result, 0)
	return result
}

func order(cur *TreeNode, result *[][]int, depth int) {
	if cur == nil {
		return
	}
	if len(*result) == depth {
		*result = append(*result, []int{})
	}
	(*result)[depth] = append((*result)[depth], cur.Val)
	order(cur.Left, result, depth+1)
	order(cur.Right, result, depth+1)
}
```

---

### [107. Binary Tree Level Order Traversal II]  

跟上一題 102 一樣的做法，最後將答案反轉即可。

**Iteration Solution:**
```go
func levelOrderBottom(root *TreeNode) [][]int {
	var result [][]int
	var queue []*TreeNode
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size int = len(queue)
		var level []int
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			level = append(level, cur.Val)
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
		result = append(result, level)
	}
	reserve(&result)
	return result
}

func reserve(arr *[][]int) {
	for i, j := 0, len(*arr)-1; i < j; {
		(*arr)[i], (*arr)[j] = (*arr)[j], (*arr)[i]
		i++
		j--
	}
}
```

---

### [199. Binary Tree Right Side View]  

在 level order 中找到每一層的最後一個 Node 加入到答案中即可。

**Iteration Solution:**
```go
func rightSideView(root *TreeNode) []int {
	var result []int
	var queue []*TreeNode
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size int = len(queue)
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			if i == size-1 {
				result = append(result, cur.Val)
			}
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
	}
	return result
}
```

---

### [637. Average of Levels in Binary Tree]  

加入同一層的值到一個變數中，然後除以該層的 Node 數量（size）。

**Iteration Solution:**
```go
func averageOfLevels(root *TreeNode) []float64 {
	var result []float64
	var queue []*TreeNode
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size, sum int = len(queue), 0
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			sum += cur.Val
			if i == size-1 {
				result = append(result, float64(sum) / float64(size))
			}
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
	}
	return result
}
```

---

### [429. N-ary Tree Level Order Traversal]  

改變 102 題的加入子 Node 到 Queue 的方法，就是 N-ary Tree 的解法。

**Iteration Solution:**
```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func levelOrder(root *Node) [][]int {
	var result [][]int
	var queue []*Node
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size int = len(queue)
		var level []int
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			level = append(level, cur.Val)
			for _, children := range cur.Children {
				queue = append([]*Node{children}, queue...)
			}
		}
		result = append(result, level)
	}
	return result
}
```

---

### [515. Find Largest Value in Each Tree Row]  

Level order, 拿到每一層的最大值。

**Iteration Solution:**
```go
func largestValues(root *TreeNode) []int {
	var result []int
	var queue []*TreeNode
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size, maxint int = len(queue), math.MinInt
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			if cur.Val > maxint {
				maxint = cur.Val
			}
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
		result = append(result, maxint)
	}
	return result
}
```

### [116. Populating Next Right Pointers in Each Node]  
### [117. Populating Next Right Pointers in Each Node II]  

使用 level order 的方式，如果 Node 不是最後一個元素，Next 就是 Queue 的下一個元素。

**Iteration Solution:**
```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
	var queue []*Node
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0{
		var size int = len(queue)
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			if i != size-1 {
				cur.Next = queue[len(queue)-1]
			}
			if cur.Left != nil {
				queue = append([]*Node{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*Node{cur.Right}, queue...)
			}
		}
	}
	return root
}
```

### [104. Maximum Depth of Binary Tree]  

下面的解法使用遞迴，其實跟 level order 的邏輯是一樣的。

**Recursion Solution:**
```go
func maxDepth(root *TreeNode) int {
	return Recursion(root, 0)
}

func Recursion(cur *TreeNode, depth int) int {
	if cur == nil {
		return depth
	}
	return int(math.Max(float64(Recursion(cur.Left, depth+1)), float64(Recursion(cur.Right, depth+1))))
}
```
Bottom up solution, find leaf node and return 1, and +1 for each passed node after that, until it returns to the root.
```go
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(maxDepth(root.Left), maxDepth(root.Right)) +1 
}

func max(i, j int) int {
	if i > j {
		return i
	}
	return j
}
```

### [111. Minimum Depth of Binary Tree]  

比較所有的葉子節點，取最小的深度作為答案。

**Recursion Solution:**
```go
func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	var minDepth int = math.MaxInt
	Recursion(root, &minDepth, 1)
	return minDepth
}

func Recursion(cur *TreeNode, minDepth *int, depth int) {
	if cur == nil {
		return
	}
	if cur.Left == nil && cur.Right == nil {
		*minDepth = Min(*minDepth, depth)
	}
	Recursion(cur.Left, minDepth, depth+1)
	Recursion(cur.Right, minDepth, depth+1)
}

func Min(i, j int) int {
	if i > j {
		return j
	}
	return i
}
```

### [103. Binary Tree Zigzag Level Order Traversal]  

跟 Level order 一樣的邏輯，只是加入一個 Flag 來控制方向。

**Iteration Solution:**
```go
func zigzagLevelOrder(root *TreeNode) [][]int {
	var result [][]int
	var queue []*TreeNode
	var flag int = 1
	if root != nil {
		queue = append(queue, root)
	}
	for len(queue) > 0 {
		var size int = len(queue)
		var level []int
		for i := 0; i < size; i++ {
			cur := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			level = append(level, cur.Val)
			if cur.Left != nil {
				queue = append([]*TreeNode{cur.Left}, queue...)
			}
			if cur.Right != nil {
				queue = append([]*TreeNode{cur.Right}, queue...)
			}
		}
		if flag == 1 {
			result = append(result, level)
			flag++
		} else {
			reverse(level)
			result = append(result, level)
			flag--
		}
	}
	return result
}

func reverse(arr []int) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}
```

---

### [2583. Kth Largest Sum in a Binary Tree]

看到題目就覺得要用 Level Order，這裡直接把每層的和加入到一個 Array 中，然後排序取 Kth 的值。

**Iteration Solution:**
-	這裡偷懶用 sort.Slice 來排序，應該可以用其他方法來加速
```go
func kthLargestLevelSum(root *TreeNode, k int) int64 {
    sum := []int64{}
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        size := len(queue)
        var temp int64 = 0
        for i := 0; i < size; i++ {
            cur := queue[i]
            temp += int64(cur.Val)
            if cur.Left != nil {
                queue = append(queue, cur.Left)
            }
            if cur.Right != nil {
                queue = append(queue, cur.Right)
            }
        }
        sum = append(sum, temp)
        queue = queue[size:]
    }

	sort.Slice(sum, func(i, j int) bool {
		return sum[i] > sum[j]
	})
    
    if k > len(sum) {
        return -1
    }
    return sum[k-1]
}
```

[reference]: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.md
[102. Binary Tree Level Order Traversal]: https://leetcode.com/problems/binary-tree-level-order-traversal/
[107. Binary Tree Level Order Traversal II]: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
[199. Binary Tree Right Side View]: https://leetcode.com/problems/binary-tree-right-side-view/
[637. Average of Levels in Binary Tree]: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
[429. N-ary Tree Level Order Traversal]: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
[515. Find Largest Value in Each Tree Row]: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
[116. Populating Next Right Pointers in Each Node]: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
[117. Populating Next Right Pointers in Each Node II]: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
[104. Maximum Depth of Binary Tree]: https://leetcode.com/problems/maximum-depth-of-binary-tree/
[111. Minimum Depth of Binary Tree]: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
[103. Binary Tree Zigzag Level Order Traversal]: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
[2583. Kth Largest Sum in a Binary Tree]: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/