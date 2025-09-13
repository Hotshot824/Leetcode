---
Category: Binary Tree
Subcategory: Binary tree
Title: Recursion Binary traversal
Date: 2025-09-12
Difficulty: Easy
Status: Accepted
---

### Recursion Binary traversal 

Inorder, Preorder and Postorder, Using recursion. [reference]  
Description of the three orders [wikipedia].  

Traversing a binary tree recursively requires attention to the following steps:  
1. Determine the parameters and return value of a recursive function.
2. Determine the termination condition.
3. Determine the logic for a single level of recursion.

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

[94. Binary Tree Inorder Traversal]  
```go
func inorderTraversal(root *TreeNode) []int {
	var result []int
	traversal(root, &result)
	return result
}

func traversal(cur *TreeNode, result *[]int) {
	if cur == nil {
		return
	}
	traversal(cur.Left, result)
	*result = append(*result, cur.Val)
	traversal(cur.Right, result)
}
```

[144. Binary Tree Preorder Traversal]  
```go
func preorderTraversal(root *TreeNode) []int {
	var result []int
	traversal(root, &result)
	return result
}

func traversal(cur *TreeNode, result *[]int) {
	if cur == nil {
		return
	}
	*result = append(*result, cur.Val)
	traversal(cur.Left, result)
	traversal(cur.Right, result)
}
```

[145. Binary Tree Postorder Traversal]  
```go
func postorderTraversal(root *TreeNode) []int {
	var result []int
	traversal(root, &result)
	return result
}

func traversal(cur *TreeNode, result *[]int) {
	if cur == nil {
		return
	}
	traversal(cur.Left, result)
	traversal(cur.Right, result)
	*result = append(*result, cur.Val)
}
```

[94. Binary Tree Inorder Traversal]: https://leetcode.com/problems/binary-tree-inorder-traversal/
[144. Binary Tree Preorder Traversal]: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
[145. Binary Tree Postorder Traversal]: https://leetcode.com/problems/binary-tree-postorder-traversal/
[wikipedia]: https://en.wikipedia.org/wiki/Tree_traversal
[reference]: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.md