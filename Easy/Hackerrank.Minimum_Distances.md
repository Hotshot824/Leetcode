---
Category: Array
Subcategory: Array
Title: Hackerrank. Minimum Distances
Date: 2025-12-04
Difficulty: Easy
Status: Accepted
---

### [Hackerrank. Minimum Distances]

[Hackerrank. Minimum Distances]: https://www.hackerrank.com/challenges/minimum-distances/problem

給一個 Array，找出陣列中兩個相同數字之間的最短距離，反回這個距離，如果沒有相同數字則回傳 -1。

### Brute Force Solution

最直接寫法就是雙層迴圈，找出所有相同數字的距離，然後取最小值。

Time Complexity O(n<sup>2</sup>), Space Complexity O(1).

**C Solution:**
```c
/*
 * Complete the 'minimumDistances' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int minimumDistances(int a_count, int* a) {
    int res = INT_MAX;
    for (int i = 0; i < a_count; i++) {
        for (int j = i+1; j < a_count; j++) {
            if (a[i] == a[j]) {
                res = MIN(res, j-i);
            }
        }
    }
    return res == INT_MAX ? -1 : res;
}
```

### Hash Map Solution

使用一個 Hash Map 來記錄每個數字上次出現的位置，當再次遇到相同數字時，計算距離並更新最小值。
這樣就只需要一次掃描，在掃描的時候檢查 Hash Map 更新 Result，並在最後更新 Hash Map。

Time Complexity O(n), Space Complexity O(n).

**C Solution:**
```c
/*
 * Complete the 'minimumDistances' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */
#define MIN(a,b) ((a) < (b) ? (a) : (b))

#define SIZE 100001

int minimumDistances(int a_count, int* a) {
    int hash[SIZE];
    memset(hash, -1, sizeof(hash));
    
    int res = INT_MAX;
    for (int i = 0; i < a_count; i++) {
        int v = a[i];
        
        if (hash[v] != -1) {
            res = MIN(res, i - hash[v]);
        } 
        hash[v] = i;    
    }
    
    return res == INT_MAX ? -1 : res;
}
```