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

-	2: `1`, 3: `2`
-	4: `1`, 5: `2`, 6: `2`, 7: `3`
-	8: `1`, 9: `2`, 10: `2`, 11: `3`, 12: `2`, 13: `3`, 14: `3`, 15: `4`

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

---

### [268. Missing Number]

這題如果想要在 O(n) 的時間複雜度內解決，就需要用上 bitwise 的方式，詳情可見 [Comments from Carinananaljr]。

-	對於任何一個數字 a，對於 b 進行兩次 XOR 將會 `a^b^b = a`
-	因此我們假設這裡有 `3, 0, 1` 這個缺少 2 的 array
	-	**3^0^1^3^0^1^2 = 2**

Time Complexity: O(n)

Solution:
```go
func missingNumber(nums []int) int {
	var xor, i int = 0, 0
	for ; i < len(nums); i++ {
		xor = xor ^ i ^ nums[i]
	}
	return xor ^ i
}
```

這邊也可以利用數學方式，等差數列求和的方式來解決這個問題 1 ~ n 的和為 `n*(n+1)/2`，所以缺少的數字就是 `n*(n+1)/2 - sum`。

Solution 2:
```go
func missingNumber(nums []int) int {
	var sum int
	for _, v := range nums {
		sum += v
	}
	return (len(nums)+1)*len(nums)/2 - sum
}
```

[268. Missing Number]: https://leetcode.com/problems/missing-number/
[Comments from Carinananaljr]: https://leetcode.com/problems/missing-number/solutions/69791/4-line-simple-java-bit-manipulate-solution-with-explaination/comments/148758

---

### [136. Single Number]

同上題這裡也利用了 XOR 的特性，a^a = 0，所以對於任何一個數字，對它進行兩次 XOR 將會得到 0

Time Complexity: O(n)

Solution:
```go
func singleNumber(nums []int) int {
    var xor int = 0
    for _, v := range nums {
        xor ^= v
    }
    return xor
}
```

[136. Single Number]: https://leetcode.com/problems/single-number/