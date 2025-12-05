---
Category: Math
Subcategory: Math
Title: Hackerrank. Grading Students
Date: 2025-12-04
Difficulty: Easy
Status: Accepted
---

### [Hackerrank. Grading Students]

[Hackerrank. Grading Students]: https://www.hackerrank.com/challenges/grading/problem

這題的要求是給一個學生分數的陣列，然後根據以下規則來調整分數:
-   跟下一個 5 的倍數差距小於 3 分，則將分數調整到下一個 5 的倍數，否則分數不變。
-   分數低於 38 分不做調整，因為這樣學生還是會不及格。

---

### Mathematical Solution

要思考的是怎麼快速算出跟下一個 5 的倍數的差距，可以用以下的數學方式來計算:
-   反向把原始分數直接 + 5 然後 mod 5，這樣得到的就是分數到下一個 5 的多出來的部分。
    -   例如分數是 84 分，(84 + 5) % 5 = 4，代表距離下一個 5 的倍數 85 還多出來 4 分。
-   如果這個多出來的部分 >= 3，就代表距離下一個 5 的倍數差距小於 3 分，可以進行調整。
    -   把原始分數加上 (5 - diff) 就是調整後的分數。

Time Complexity O(n), Space Complexity O(1).

**C Solution:**
```c
int* gradingStudents(int grades_count, int* grades, int* result_count) {
    for (int i = 0; i < grades_count; i++) {
        if (grades[i] < 38) {
            continue;
        }
        int diff = (grades[i] + 5) % 5;
        if (diff >= 3) {
            grades[i] = grades[i] + 5 - diff;
        }
    }
    *result_count = grades_count;
    return grades;
}
```