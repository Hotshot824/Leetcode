### Binary Tree Level Order Traversal

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

[102. Binary Tree Level Order Traversal]: https://leetcode.com/problems/binary-tree-level-order-traversal/
[107. Binary Tree Level Order Traversal II]: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/