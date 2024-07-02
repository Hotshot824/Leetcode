### [2215. Find the Difference of Two Arrays]

最簡單的方法就是用 hash table 來記錄兩個 array 的元素，然後比較兩個 hash table 的差異即可。

Time Complexity O(n+m), Space Complexity O(n+m).

**Solution:**
```go
func findDifference(nums1 []int, nums2 []int) [][]int {
    h1, h2 := map[int]bool{}, map[int]bool{}
    for _, n := range nums1 {
        h1[n] = true
    }
    for _, n := range nums2 {
        h2[n] = true
    }
    result := [][]int{{}, {}}
    for k := range h1 {
        if ok, _ := h2[k]; !ok {
            result[0] = append(result[0], k)
        }
    }
    for k := range h2 {
        if ok, _ := h1[k]; !ok {
            result[1] = append(result[1], k)
        }
    }
    return result
}
```

[2215. Find the Difference of Two Arrays]: https://leetcode.com/problems/find-the-difference-of-two-arrays