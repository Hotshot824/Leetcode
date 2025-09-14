---
Category: Math
Subcategory: Math
Title: Hackerrank. Non-Divisible Subset
Date: 2025-09-15
Difficulty: Medium
Tag: Math, Hash
Status: Accepted
---

### [Hackerrank. Non-Divisible Subset]

[Hackerrank. Non-Divisible Subset]: https://www.hackerrank.com/challenges/non-divisible-subset/problem

這題是給定一個 Integer Array 和一個 Integer K，找出 Array 裡面最大的 Subset，
該 Subset 需要滿足 Subset 裡面任兩個數字的和都不能被 K 整除。

---

### Math

這題要用數學的方式來解，如果 a + b 能被 K 整除，那麼必然 (a + b) % K == 0。

首先這題求的是 Subset 的大小，所以我們不需要真的把 Subset 找出來，只需要知道 Subset 裡面有多少個數字就好。
那我們就可以把 Array 裡面的數字都對 K 取餘數，然後統計每個餘數出現的次數。

得到以下規則:
1. Remainder 0 的數字只能選一個
    -   因為兩個 `Remainder 0` 的數字相加會導致 a + b 能被 K 整除
2. Remainder K/2 的數字只能選一個，如果 K 是偶數
    -   因為兩個 `Remainder = K/2` 的數字相加會導致 a + b 能被 K 整除
    -   例如: K = 4 就不可能找兩個餘數是 2 的數字，因為 2 + 2 = 4 能被 4 整除
3. Remainder i 和 Remainder K-i 的數字只能選一種
    -   因為 `Remainder i` 和 `Remainder K-i` 的數字相加會導致 a + b 能被 K 整除

最後我們就可以根據以上規則來計算 Subset 的大小。

Example:

Array = [1, 7, 2, 4, 3], K = 3

1. 計算出所有數字對 K 取餘數的結果
    -   Remainder = [1, 1, 2, 1, 0]
2. 統計每個餘數出現的次數
    -   Count = [1, 3, 1]
3. 根據規則計算 Subset 的大小
    1.  Remainder 0 的數字只能選一個，所以 Subset 大小 +1
    2.  K 是奇數，所以不需要考慮 Remainder K/2 的情況
    3.  (i, K-i) = (1, 2)，在這兩種餘數互補種只能求一種
        -   max(Count[1], Count[2]) = max(3, 1) = 3
4. 最後 Subset 的大小 = 1 + 3 = 4

Time Complexity O(N), Space Complexity O(K).

**CPP Solution:**
```cpp
int nonDivisibleSubset(int k, vector<int> s) {
    vector<int> count(k, 0);
    for (int num : s) {
        count[num % k]++;
    }
    
    int result = 0;
    
    if (count[0]) result++;
    
    for (int r = 1; r <= k/2; r++) {
        if (r == k - r) {
            result++;
        } else {
            result += std::max(count[r], count[k-r]);
        }
    } 
    
    return result;
}
```

**Golang Solution:**
```go
func nonDivisibleSubset(k int32, s []int32) int32 {
    count := make([]int32, k)
    for _, num := range s {
        count[num % k]++
    }
    
    var res int32 = 0
    
    if (count[0] > 0) {
        res++
    }
    
    for r := int32(1); r <= k/2; r++ {
        if (r == k-r) {
            res++
        } else {
            res += max(count[r], count[k-r])
        }
    }
    
    return res
}
```