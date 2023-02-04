### Build Binary Tree for Array

> Using Array to build a binary tree, to test leetocde problem.

1. Root must be index 1.
2. Current Node left child is Current Node `index*2`, Right child is the `index*2+1`

Build a binary tree with the above conditions.

```go
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func Constructor(arr []int) *TreeNode {
	arr = append([]int{0}, arr...)
	return buildTree(arr, 1)
}

func buildTree(arr []int, index int) *TreeNode {
	if index >= len(arr) {
		return nil
	}
	node := &TreeNode{Val: arr[index]}
	node.Left = buildTree(arr, index*2)
	node.Right = buildTree(arr, index*2+1)
	return node
}
```

If arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}, this binary tree is as shown below:  
```
        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  / \
 8   9 
```

Can use leetcode Tree travesal to check:  
[Recursion Binary traversal]

[Recursion Binary traversal]: https://github.com/Hotshot824/Leetcode/blob/main/Easy/Recursion_Binary_Tree_Traversal.md.md