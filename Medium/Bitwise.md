---
Category: Bit Manipulation
Subcategory: Bit Manipulation
Title: Bit Manipulation Summary
Date: 2025-09-12
Difficulty: Medium
Status: Accepted
---

### [231. Power of Two]

1.  如果一個數是 2 的次方數，那麼它的 Binary 只會有一個 1
    -   8: `1000`, 16: `10000
2.  所以直接 AND `n-1` 必然會得到 0
3.  這裡要注意的是 0 不是 2 的次方數，所以要特別處理

**Solution:**
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

**Solution:**
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

**Solution:**
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

**Solution 2:**
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

**Solution:**
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

---

### [89. Gray Code]

這邊要看下 Gray Code 的規則，對於 n = 2 的情況，`00, 01, 11, 10`，可以看到這個規則是對稱的，所以可以利用 XOR 的方式來解決這個問題。

**Solution:**
```go
func grayCode(n int) []int {
    res := []int{}
    for i := 0; i < pow(2, n); i++ {
        res = append(res, i^(i>>1))
    }
    return res
}

func pow(base, exponent int) int {
    result := 1
    for exponent != 0 {
        if exponent%2 != 0 {
            result *= base
        }
        base *= base
        exponent /= 2
    }
    return result
}
```

[89. Gray Code]: https://leetcode.com/problems/gray-code/

---

### [2419. Longest Subarray With Maximum Bitwise AND]

這題雖然被分類在 Bit Manipulation，但是實際上是一個 sliding window 的問題，先釐清找到 Longest Subarray with Maximum Bitwise AND 的條件。
實際上就是在這個 Array 中找到連續的最大值，如果不是最大值都將會因為 AND 的特性使得結果變小。

這樣我們就能用 Two pointer 來解這題:
1.	初始化變數
	-	Res: 紀錄最大的 Subarray 長度
	-	Maximum: 紀錄目前最大的數字
2.	遍歷整個 Array 並使用 Left, Right 兩個 Pointer
	-	Arr.Left > Maximum，更新 Maximum，並將 Left 設為 Right，Res 設為 1 代表找到一個 Subarray
	-	Arr.Left = Maximum，更新 Res = max(Res, Right - Left + 1)
	-	Arr.Left < Maximum，將 Left 設為 Right+1，代表重新開始找 Subarray

Time Complexity O(n), Space Complexity O(1).

**Solution:**
```go
func longestSubarray(nums []int) int {
    res := 0
    maximum := 0

    left := 0
    for right := range nums {
        if nums[right] > maximum {
            maximum = nums[right];
            left = right;
            res = 1;
        } else if nums[right] == maximum {
            res = max(res, right - left + 1)
        } else {
            left = right+1;
        }
    }
    return res
}
```

[2419. Longest Subarray With Maximum Bitwise AND]: https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/