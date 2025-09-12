---
Category: Binary Tree
Subcategory: binary tree
Title: N-ary Tree Traversal
Date: 2025-09-12
Difficulty: Easy
Status: Accepted
---

### N-ary Tree Traversal

Reference [Recursion Binary Tree Traversal] and [Iteration Binary Tree Traversal].  
Using Recursion and Iteration to solution.

### [589. N-ary Tree Preorder Traversal]  

Preorder is `Middle -> Left -> Right`, So using this order add node in stack.
1. Add root in stack
2. Stack pop and join cur in result.
3. Join child in stack from right to left
4. Keep step 1~3 until stack is empty

**Iteration:**
```go
func preorder(root *Node) []int {
	var result []int
	var stack []*Node
	if root != nil {
		stack = append(stack, root)
	}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, cur.Val)
		for i := len(cur.Children) - 1; i >= 0; i-- {
			stack = append(stack, cur.Children[i])
		}
	}
	return result
}
```

**Recursion**
```go
func preorder(root *Node) []int {
	var result []int
	order(root, &result)
	return result
}

func order(cur *Node, result *[]int) {
	if cur == nil {
		return
	}
	*result = append(*result, cur.Val)
	for _, children := range cur.Children {
		order(children, result)
	}
}
```

---

### [590. N-ary Tree Postorder Traversal]  

**Reverse Preorder Answer**
Preorder is `Middle -> Left -> Right`, Postorder is `Left -> Right -> Middle`, 
So change preorder operation to `Middle -> Right -> Left`,
then reverse when get Postorder answer.  

**Iteration**
```go
func postorder(root *Node) []int {
	var result []int
	var stack []*Node
	if root != nil {
		stack = append(stack, root)
	}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, cur.Val)
		stack = append(stack, cur.Children...)
	}
	reverse(&result)
	return result
}

func reverse(arr *[]int) {
	for i, j := 0, len(*arr)-1; i < j; i, j = i+1, j-1 {
		(*arr)[i], (*arr)[j] = (*arr)[j], (*arr)[i]
	}
}
```

**Recursion**
```go
func postorder(root *Node) []int {
	var result []int
	order(root, &result)
	reverse(&result)
	return result
}

func order(cur *Node, result *[]int) {
	if cur == nil {
		return
	}
	*result = append(*result, cur.Val)
	for i := len(cur.Children) - 1; i >= 0; i-- {
		order(cur.Children[i], result)
	}
}

func reverse(arr *[]int) {
	for i, j := 0, len(*arr)-1; i < j; i, j = i+1, j-1 {
		(*arr)[i], (*arr)[j] = (*arr)[j], (*arr)[i]
	}
}
```

**Postorder**

Using postorder to traversal tree: 
1. Traversal child order is from left to right 
2. If all child traversed join cur in result

**Recursion:**
```go
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
    var result []int
    postorderTraversal(root, &result)
    return result
}

func postorderTraversal(cur *Node, result *[]int) {
    if cur == nil {
        return
    }
    for _, child := range cur.Children {
        postorderTraversal(child, result)
    }
    *result = append(*result, cur.Val)
}
```

[589. N-ary Tree Preorder Traversal]: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
[590. N-ary Tree Postorder Traversal]: https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/