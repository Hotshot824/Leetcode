---
Category: Math
Subcategory: Math
Title: Hackerrank. Apple and Orange
Date: 2025-12-04
Difficulty: Easy
Status: Accepted
---

### [Hackerrank. Apple and Orange]

[Hackerrank. Apple and Orange]: https://www.hackerrank.com/challenges/apple-and-orange/problem

這題一定要看好敘述，題目給了一個區間 [s, t] 代表房子的位置，然後給了兩個樹的位置 a, b，分別是蘋果樹和橘子樹。
接著給了兩個陣列分別代表蘋果和橘子掉落的位置，**這些位置是相對於樹的位置來計算的**。

所以 apples 跟 oranges 陣列裡面的數字，正數代表往右掉落，負數代表往左掉落。

### Mathematical Solution

這題的解法很簡單，就是把每個蘋果和橘子掉落的位置加上樹的位置，然後檢查是否在區間 [s, t] 之內。

Time Complexity O(n), Space Complexity O(1).

**C Solution:**
```c
/*
 * Complete the 'countApplesAndOranges' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER s
 *  2. INTEGER t
 *  3. INTEGER a
 *  4. INTEGER b
 *  5. INTEGER_ARRAY apples
 *  6. INTEGER_ARRAY oranges
 */
void countApplesAndOranges(int s, int t, int a, int b, int apples_count, int* apples, int oranges_count, int* oranges) {
    int r1 = 0, r2 = 0;
    for (int i = 0; i < apples_count; i++) {
        int d = a + apples[i];
        if (d >= s && d <= t) {
            r1++;
        }
    }
    for (int i = 0; i < oranges_count; i++) {
        int d = b + oranges[i];
        if (d >= s && d <= t) {
            r2++;
        }
    }
    printf("%d\n%d\n", r1, r2);
}
```


