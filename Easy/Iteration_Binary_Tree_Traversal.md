### Iteration Binary Tree Traversal

Inorder, Preorder and Postorder, Using iteration. [reference]  
Description of the three orders [wikipedia].  

Iteration to Binary Tree is using Stack to traverse Binary Tree, Detial watch diagram:  

1. Inorder is `Left -> Middle -> Right`, Because Left is first. So we need two steps:
    1. Traversal Node and add Node to stack first, until point reach the bottom.
    2. Then process the stack.
2. Preorder is `Middle -> Left -> Right`, so push in stack order is Right -> Left, because stack is first in last out.
3. Postorder is `Left -> Right -> Middle`, We can chang Preoredr stack order `Middle -> Left -> Right` to `Middle -> Right -> Left`,
then reverse result is `Left -> Right -> Middle` is answer.

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
![Inorder diagram]
```go
func inorderTraversal(root *TreeNode) []int {
	var result []int
	var stack []*TreeNode
	cur := root
	for len(stack) > 0 || cur != nil {
		if cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		} else {
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result = append(result, cur.Val)
			cur = cur.Right
		}
	}
	return result
}
```

[144. Binary Tree Preorder Traversal]  
![Proeorder diagram]
```go
func preorderTraversal(root *TreeNode) []int {
	var result []int
	if root == nil {
		return result
	}
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, node.Val)
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
	}
	return result
}
```

[145. Binary Tree Postorder Traversal]  
![Postorder diagram]  
```go
func postorderTraversal(root *TreeNode) []int {
	var result []int
	if root == nil {
		return result
	}
	var stack []*TreeNode
	stack = append(stack, root)
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		result = append(result, node.Val)
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
	}
	reverse(&result)
	return result
}

func reverse(arr *[]int) {
	for i, j := 0, len(*arr)-1; i < j; {
		(*arr)[i], (*arr)[j] = (*arr)[j], (*arr)[i]
		i++
		j--
	}
}

```

[94. Binary Tree Inorder Traversal]: https://leetcode.com/problems/binary-tree-inorder-traversal/
[144. Binary Tree Preorder Traversal]: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
[145. Binary Tree Postorder Traversal]: https://leetcode.com/problems/binary-tree-postorder-traversal/
[wikipedia]: https://en.wikipedia.org/wiki/Tree_traversal
[reference]: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%BF%AD%E4%BB%A3%E9%81%8D%E5%8E%86.md
[Inorder diagram]: https://camo.githubusercontent.com/6ea32e330a3c937346b1f48b3808a3ab0aade0f9b3cbe4a93b5580c08727cdb1/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f2545342542412538432545352538462538392545362541302539312545342542382541442545352542412538462545392538312538442545352538452538362545462542432538382545382542462541442545342542422541332545362542332539352545462542432538392e676966
[Proeorder diagram]: https://camo.githubusercontent.com/b9924e53ce35c0417f176da66bcac1738f75eeb2ab20f4f243c36be62295004a/68747470733a2f2f636f64652d7468696e6b696e672e63646e2e626365626f732e636f6d2f676966732f2545342542412538432545352538462538392545362541302539312545352538392538442545352542412538462545392538312538442545352538452538362545462542432538382545382542462541442545342542422541332545362542332539352545462542432538392e676966
[Postorder diagram]: https://camo.githubusercontent.com/fb9492d2de573a3b93e13c1dbad73e2d799eb50dc54c10a82ea34d97fac27913/68747470733a2f2f696d672d626c6f672e6373646e696d672e636e2f32303230303830383230303333383932342e706e67