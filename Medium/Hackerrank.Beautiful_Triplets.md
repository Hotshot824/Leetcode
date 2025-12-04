---
Category: Two Pointer
Subcategory: Two Pointer
Title: Hackerrank. Beautiful Triplets
Date: 2025-12-04
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Beautiful Triplets]

[Hackerrank. Beautiful Triplets]: https://www.hackerrank.com/challenges/beautiful-triplets/problem

這題的要求是在一個 Sequence 裡面找出有多少 3 tuple (i, j, k) 符合以下兩個條件:
1.  i < j < k
2.  arr[j] - arr[i] = d 且 arr[k] - arr[j] = d

### Two Pointer Solution

這題第一時間先想到類似 3Sum 的解法，用 HashSet 來記錄需要的數字，然後歷變陣去找符合條件的三元組。
但這裡有個可以用 Two Pointer 的解法，因為題目已經有給定 arr 是排序過的陣列，所以我們可以用三個指標 i, j, k 來遍歷陣列。
這比較接近 O(n<sup>2</sup>) 的解法，比起 O(n) 的 HashSet 解法在時間複雜度上沒有優勢，但在空間複雜度上會比較好。

Time Complexity O(n<sup>2</sup>), Space Complexity O(1).

**C Solution:**
```c
/*
 * Complete the 'beautifulTriplets' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */
int beautifulTriplets(int d, int arr_count, int* arr) {
    int res = 0;
    for (int i = 0; i < arr_count; i++) {
        int j = i + 1;
        while (j < arr_count && arr[j] < arr[i] + d) {
            j++;
        }
        if (j >= arr_count || arr[j] != arr[i] + d) continue;

        int k = j + 1;
        while (k < arr_count && arr[k] < arr[j] + d) {
            k++;
        }
        if (k >= arr_count || arr[k] != arr[j] + d) continue;

        res++;
    }
    return res;
}
```

**GO Solution:**
```go
func beautifulTriplets(d int32, arr []int32) int32 {
    res := 0
    for i := 0; i < len(arr); i++ {
        j := i + 1
        for j < len(arr) && arr[j] < arr[i] + d {
            j++
        }
        if j >= len(arr) || arr[j] != arr[i] + d {
            continue
        }
        k := j + 1
        for k < len(arr) && arr[k] < arr[j] + d {
            k++
        }
        if k >= len(arr) || arr[k] != arr[j] + d {
            continue
        }
        res++
    }
    return int32(res)
}
```

### HashSet Solution

這是比較類似於 3Sum 的解法，利用 HashSet 來記錄陣列中的數字，然後再遍歷陣列去找符合條件的三元組。

我們知道要滿足條件就需要有 arr[i], arr[i] + d, arr[i] + 2d 這三個數字存在於陣列中。
所以我們可以先把陣列的數字放到一個 HashSet 裡面，然後再遍歷陣列，對每一個數字 arr[i]，
我們檢查 arr[i] + d 和 arr[i] + 2d 是否存在於 HashSet 裡面，若存在則 Res++。

但要注意我們還要另外處裡重複的問題，因為題目要求的是三元組的數量，而不是三元組的組合數量。

-   以這個例子為例 `[1, 2, 2, 3, 3], d = 1`
    -   1 可以有 (0, 1, 3), (0, 1, 4), (0, 2, 3), (0, 2, 4) 四總組合
-   直接把 hash[2] * hash[3] 相乘就是所有組合數量

#### Algorithm

1. Create a hash map to store the frequency of each number in the array.
2. Initialize a result counter to 0.
3. Iterate through each number in the array:
   - For each number `v`, check if `v + d` and `v + 2d` exist in the hash map.
   - If they exist, increment the result counter by the product of their frequencies: `hash[v + d] * hash[v + 2d]`.
4. Return the result counter.

Time Complexity O(2n) = O(n), Space Complexity O(n).

**GO Solution:**
```go
/*
 * Complete the 'beautifulTriplets' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

func beautifulTriplets(d int32, arr []int32) int32 {
    hash := map[int32]int32{}
    for _, v := range arr {
        hash[v]++
    }
    
    res := int32(0)
    for _, v := range arr {
        res += hash[v+d] * hash[v+d*2]
    }
    return res
}
```

**C Solution:**
```c
/*
 * Complete the 'beautifulTriplets' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */
#define MAX (int)2e4 + 21

int beautifulTriplets(int d, int arr_count, int* arr) {
    int hash[MAX] = {0};
    
    for (int i = 0; i < arr_count; i++) {
        hash[arr[i]]++;
    }
        
    int res;
    for (int i = 0; i < arr_count; i++) {
        int x = arr[i];
        if (x + d < MAX && x + 2*d < MAX) {
            res += hash[x + d] * hash[x + 2*d];
        }
    }
    return res;
}
```