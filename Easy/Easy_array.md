### Easy Array

跟 Array 相關的題目，主要是要熟悉 Array 的操作，例如：新增、刪除、修改、查詢等等，到更進階的 two pointer、sliding window 等。
但是 Easy 的題目通常不會太複雜，所以不需要太多的技巧，只要熟悉基本的操作就可以了。

### [2864. Maximum Odd Binary Number]

最大的 Odd Binary 一定是以 1 結尾，所以保留一個 1 剩下的 1 全部排到前面，後面補 0 即可。

**Solution:**
```go
func maximumOddBinaryNumber(s string) string {
    ret := ""
    for i := range s {
        if s[i] == '1' {
            ret = "1" + ret
        } else {
            ret = ret + "0"
        }
    }
    ret = ret[1:]
    ret = ret + "1"
    return ret
}
```

[2864. Maximum Odd Binary Number]: https://leetcode.com/problems/maximum-odd-binary-number/

### [58. Length of Last Word]

直接從後面找到第一個不是空白的字元，然後開始計算長度，直到遇到空白字元或是字串結束。

**Solution:**
```go 
func lengthOfLastWord(s string) int {
    count := 0
    for i := len(s)-1; i >= 0; i-- {
        if s[i] != ' ' {
            count++
        }
        if s[i] == ' ' && count != 0 {
            return count
        }
    }
    return count
}
```

[58. Length of Last Word]: https://leetcode.com/problems/length-of-last-word/

---

### [88. Merge Sorted Array]

#### Two Pointer

因為這題的 nums1 的長度是 m+n，nums2 則是 n，所以是特別設計給 nums1 的空間可以容納 nums2 的元素。
這樣的可以特別設計這樣的算法來處理合併排序:
-   直接從 nums1 的尾巴往前比較，使用 nums1[m+n-1] 放置元素
    -   依序把 nums1[m-1] 和 nums2[n-1] 比較，大的放在 nums1[m+n-1]
-   如果 n 先結束，則不用處理，因為 nums1 已經是排序好的

Time Complexity O(n+m), Space Complexity O(1)

**Solution:**
```go
func merge(nums1 []int, m int, nums2 []int, n int)  {
    if n <= 0 {
        return
    }
    for n > 0 {
        if m > 0 && nums1[m-1] > nums2[n-1] {
            nums1[m+n-1] = nums1[m-1]
            m--
        } else {
            nums1[m+n-1] = nums2[n-1]
            n--
        }
    }
}
```

#### Directly Merge and Sort

Golang 偷懶的寫法，直接把 nums2 的元素 append 到 nums1，然後排序即可。
-   這裡要注意的是因為用的是 slice 所以要注意如果合併後 size 超過 m，會導致底層分配新的 address
    -   直接拿 nums1 後半 m 數量的 element 來跟 nums2 合併就好

Time Complexity O(mlogm), Space Complexity O(1).

**Solution**
```go
func merge(nums1 []int, m int, nums2 []int, n int)  {  
    nums1 = append(nums1[:m], nums2...)
    sort.Ints(nums1)
}
```

[88. Merge Sorted Array]: https://leetcode.com/problems/merge-sorted-array/

---

### [551. Student Attendance Record I]

很簡單的題目，只要檢查 A 的數量和 L 的數量即可，如果 A >= 2 或是 L >= 3 就回傳 false，
因為 L 是連續的，所以不是 L 的話就把 L 歸零。

**Solution:**
```go
func checkRecord(s string) bool {
    A, L := 0, 0
	for _, r := range s {
        switch r {
            case 'L':
                L++
                if L >= 3 {
                    return false
                }
            case 'A':
                A++
                if A >= 2 {
                    return false
                }
                fallthrough
            default:
                L = 0
        }
	}
	return true
}
```

[551. Student Attendance Record I]: https://leetcode.com/problems/student-attendance-record-i/

---

### [1550. Three Consecutive Odds]

在一個 Array 中尋找連續的三個奇數，如果有就回傳 true，否則回傳 false。
-   這題蠻簡單的，所以一開始就寫了下面的解法

Time Complexity O(n).

**Solution:**
```go
func threeConsecutiveOdds(arr []int) bool {
	count := 0
	for _, n := range arr {
		if n%2 > 0 {
			count++
		} else if count < 3 {
            count = 0
        } else {
            return true
        }
	}

    if count >= 3 {
        return true
    }
    return false
}
```

本來想寫 Unrolling 來加速，但是在這裡其實沒有太大的差別，因為要檢查的是 Consecutive odds，
所以 i 不是 3 個一組的話反而每個 i 要處理更多的指令，所以沒有太大的差別。

**Solution 2:**
```go
func threeConsecutiveOdds(arr []int) bool {
    size := len(arr)
    for i := 2; i < size; i++ {
        if arr[i]%2 != 0 && arr[i-1]%2 != 0 && arr[i-2]%2 != 0 {
            return true
        }
    }
    return false
}
```

[1550. Three Consecutive Odds]: https://leetcode.com/problems/three-consecutive-odds/

---

### [1460. Make Two Arrays Equal by Reversing Subarrays]

這題不要往複雜了想，如果一個 Array 跟另一個 Array 在 Sorting 後是相同的，那就絕對可以透過 Reverse Subarrays 來讓兩個 Array 相等。
但是如果真的去做 Sorting 的話，Time Complexity 就會變成 O(nlogn)，所以這裡可以用一個簡單的方法來解這題。

-   只要兩個 Array 的元素出現的次數是相同的，那就是可以透過 Reverse Subarrays 來讓兩個 Array 相等

Time Complexity O(n), Space Complexity O(1).

**Cpp Solution:**
```cpp
class Solution {
public:
    bool canBeEqual(std::vector<int>& target, std::vector<int>& arr) {
        if (target.size() != arr.size()) {
            return false;
        }

        std::array<int, 1001> targetCount = {0};
        std::array<int, 1001> arrCount = {0};

        for (int num : target) 
            targetCount[num]++;

        for (int num : arr) 
            arrCount[num]++;

        return targetCount == arrCount;
    }
};
```

[1460. Make Two Arrays Equal by Reversing Subarrays]: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

---

### [2640. Find the Score of All Prefixes of an Array]

這題先看 Score 的計算方法，Score[i] = Score[i-1] + max(nums[0], nums[1], ..., nums[i]) + nums[i]，
其實就是每次加上前一個的 Score 然後跟把目前的數字加上 max(nums[0], nums[1], ..., nums[i])。

-   應該很快能想到其實用兩個變數來紀律 Score[i-1] 和 max(nums[0], nums[1], ..., nums[i]) 即可
-   每次操作就先更新 Max Prenumber 然後加上目前的數字，再加上前一次的 Score

Time Complexity O(n), Space Complexity O(n).

**Solution**
```go
func findPrefixScore(nums []int) []int64 {
    res := make([]int64, len(nums))
    var maxPre, sumPre int64 = int64(nums[0]), 0
    for i := range nums {
        maxPre = max(maxPre, int64(nums[i]))
        cur := int64(nums[i]) + maxPre
        sumPre += cur
        res[i] = sumPre
    }
    return res
}
```

[2640. Find the Score of All Prefixes of an Array]: https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/