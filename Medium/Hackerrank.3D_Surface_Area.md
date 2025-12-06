---
Category: Math
Subcategory: Math
Title: Hackerrank. 3D Surface Area
Date: 2025-12-06
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. 3D Surface Area]

[Hackerrank. 3D Surface Area]: https://www.hackerrank.com/challenges/3d-surface-area/problem

這題會給一個 n x m 的 grid，每個格子裡面會有一個數字代表該格子的高度，要求我們計算這些立方體組成的 3D Surface Area。

---

### Mathematical Solution

最直接的操作方式是對每一個格子計算該格子的表面積，然後把所有格子的表面積加總起來。

對於一個格子的表面積計算方式如下:
-   上下面積: 2 (不管高度是多少，上下面積都是 2)
-   四個側面積: 對於每一個側面，我們需要計算該側面的高度差，如果該側面沒有相鄰的格子，則該側面的高度差就是該格子的高度。
    -   例如: 對於格子 (i, j)，其高度為 h:
        -   上側面積: max(h - height(i-1, j), 0)
        -   下側面積: max(h - height(i+1, j), 0)
        -   左側面積: max(h - height(i, j-1), 0)
        -   右側面積: max(h - height(i, j+1), 0)

因此，整個格子的表面積計算公式為:
```
surface_area(i, j) = 2 +
                    max(h - height(i-1, j), 0) +
                    max(h - height(i+1, j), 0) +
                    max(h - height(i, j-1), 0) +
                    max(h - height(i, j+1), 0)
```

Time Complexity O(n * m), Space Complexity O(1).

**C Solution:**
```c
/*
 * Complete the 'surfaceArea' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY A as parameter.
 */
int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}
 
int surfaceArea(int A_rows, int A_columns, int** A) {
    int res;
    
    for (int i = 0; i < A_rows; i++) {
        for (int j = 0; j < A_columns; j++) {
            res += 2;
            
            if (i == 0) {
                res += A[i][j];
            } else {
                res += max(A[i][j] - A[i-1][j], 0);
            }
            
            if (i == A_rows - 1) {
                res += A[i][j];
            } else {
                res += max(A[i][j] - A[i+1][j], 0);
            }
            
            if (j == 0) {
                res += A[i][j];
            } else {
                res += max(A[i][j] - A[i][j-1], 0);
            }
            
            if (j == A_columns - 1) {
                res += A[i][j];
            } else {
                res += max(A[i][j] - A[i][j+1], 0);
            }
        }
    }
    return res;
}
```
