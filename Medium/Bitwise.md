### [231. Power of Two]

1.  如果一個數是 2 的次方數，那麼它的 Binary 只會有一個 1
    -   8: `1000`, 16: `10000
2.  所以直接 AND `n-1` 必然會得到 0
3.  這裡要注意的是 0 不是 2 的次方數，所以要特別處理

```go
func isPowerOfTwo(n int) bool {
	if n == 0 {
		return false
	}
	n &= n - 1
	return n == 0
}
```

[231. Power of Two]: https://leetcode.com/problems/power-of-two/

---

### [338. Counting Bits]

這題先觀察一下 `2-3`, `4-7`, `8-15` 的計算規律

-	`2-3`
	-   2: `1`, 3: `2`
-	`4-7`
	-   4: `1`, 5: `2`, 6: `2`, 7: `3`
-	`8-15`
	-   8: `1`, 9: `2`, 10: `2`, 11: `3`, 12: `2`, 13: `3`, 14: `3`, 15: `4`

-	如果一個數字是 even，那麼它的 bit 數量會等於 nums[i/2]
-	如果一個數字是 odd，那麼它的 bit 數量會等於前一個偶數的 bit 數量加一

Solution:
```go
func countBits(n int) []int {
	result := make([]int, n+1)
	for i := 0; i < len(result); i++ {
		if i%2 == 0 {
			result[i] = result[i/2]
		} else {
			result[i] = result[i-1] + 1
		}
	}
	return result
}
```

[338. Counting Bits]: https://leetcode.com/problems/counting-bits/