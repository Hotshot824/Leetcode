### Middle Node of Linkedlist

找尋一個 Linkdelist 最快的方式是使用 fast and slow pointer，因為 fast 始終比 slow 快兩步，
所以當 fast 到達終點時 slow 就會在中點。

所以跟 Middle 有關的都可以在 Time Complexity O(n) 解決。

---

### [876. Middle of the Linked List]

最直接的題目找到中點就可以，使用 fast and slow pointer 就可以解決。

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }
    return slow
}
```

[876. Middle of the Linked List]: https://leetcode.com/problems/middle-of-the-linked-list/

---

### [2095. Delete the Middle Node of a Linked List]

跟上面的題目一樣，只是要刪除中點，所以用一個 virtual head，給 slow pointer 這樣就可以慢一個 Node，
刪除的時候就直接把 Next 指向 Next.Next 就完成了。

```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    vhead := &ListNode{Next: head}
    f, s := head, vhead
    for f != nil && f.Next != nil {
        f = f.Next.Next
        s = s.Next
    }
    s.Next = s.Next.Next
    return vhead.Next
}
```

[2095. Delete the Middle Node of a Linked List]: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

---

### Advanced Problem

##### [143. Reorder List](./143.Reorder_List.md)