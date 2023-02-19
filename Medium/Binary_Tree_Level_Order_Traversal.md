### Binary Tree Level Order Traversal

[Reference]  

Level order is using queue to traversal each level element. Because queue is `first in first out`, 
we can using this feature to design traverse function.  

Leetcode Problem:  
Golang Node struct
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
[102. Binary Tree Level Order Traversal]
There are two main steps to pay attention to in coding:  
1. Push current level Nodes child Node in queue.
2. Pop all same level Nodes and add value in result.
Iteration
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

Recursion
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
[107. Binary Tree Level Order Traversal II]  
Do it in the same way as 102, and finally reverse the answer.
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

[199. Binary Tree Right Side View]  
In level order find each level last Node add to result is the answer.
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
[637. Average of Levels in Binary Tree]  
Add same level value to a variable, then division to the level node count (size).
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
[429. N-ary Tree Level Order Traversal]  
Change problem 102. push children Node in queue method, is N-ary Tree solution.
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
[515. Find Largest Value in Each Tree Row]  
Level order, get each level max value.
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
[116. Populating Next Right Pointers in Each Node]  
[117. Populating Next Right Pointers in Each Node II]  
Using level order, if Node is not the last element, Next is the next element of the queue.
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
[104. Maximum Depth of Binary Tree]  
The following uses recursion, which is actually the same logic as level order.  
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
[111. Minimum Depth of Binary Tree]  
Compare all leaf Node, get min depth to the answer.
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
[103. Binary Tree Zigzag Level Order Traversal]  
Same logic to level order solution, but add a flag to control zigzag direction.
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
