---
Category: String
Subcategory: String
Title: Easy Hash
Date: 2025-09-12
Difficulty: Easy
Status: Accepted
---

### Easy Hash

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

---

### [1684. Count the Number of Consistent Strings]

這題如果用 Simulate 的方法解，就直接先把 allowed 裡面的字元用 hash table 來記錄，
然後再來遍歷 words，對於每個 word 的每個字元，都去檢查是否在 allowed 裡面。

Time Complexity O(n*m), Space Complexity O(1).
-   n is the length of words.
-   m is the length of word.

**Solution:**
```go
func countConsistentStrings(allowed string, words []string) int {
	hash := make([]bool, 26)
	for _, r := range allowed {
        hash[r - 'a'] = true
	}

	res := 0
	for _, word := range words {
		consistent := true
		for _, r := range word {
			if !hash[r - 'a'] {
				consistent = false
				break
			}
		}

		if consistent {
			res++
		}
	}
	return res
}
```

[1684. Count the Number of Consistent Strings]: https://leetcode.com/problems/count-the-number-of-consistent-strings