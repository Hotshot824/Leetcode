---
Category: String
Subcategory: String
Title: Hackerrank. Modified Kaprekar Numbers
Date: 2025-12-04
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Modified Kaprekar Numbers]

[Hackerrank. Modified Kaprekar Numbers]: https://www.hackerrank.com/challenges/modified-kaprekar-numbers/problem

字串處理題目，該題目有一個特別的定義，Kaprekar Number 的定義如下:

1. 將數字 n 平方，得到 d 位數的結果 (如果平方結果位數不足 d 位數，前面補 0)
2. 將平方結果分成兩個部分，右邊是 n 的位數數，左邊是剩下的部分
3. 將兩個部分相加，如果等於 n，則 n 是 Kaprekar Number

Example Number 45
-   45 的平方是 2025，45 有兩位數，所以 d = 2
-   將 2025 分成兩部分，右邊 d 位數是 25，左邊是剩餘的部分 20
-   20 + 25 = 45，所以 45 是 Kaprekar Number

要做這題要熟悉一下字串處理與數字轉換，跟分割字串的技巧，其他只要跟著題目的定義一步步做就可以了。

---

#### Algorithm

1. Set a find flag to check if any Kaprekar numbers are found.
2. Loop through each number n from p to q.
   -   Calculate the square of n.
   -   Convert the square to a string for easy manipulation.
3. Determine the number of digits d in n.
4. Split the squared string into two parts:
    -   Right part: last d digits.
    -   Left part: remaining leading digits.
5. Convert both parts back to integers (treat empty left part as 0).

Time Complexity O(n * m), where n is the range size (q - p) and m is the number of digits in the largest square.
Space Complexity O(m) for string storage.

**C Solution:**
```c
/*
 * Complete the 'kaprekarNumbers' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER p
 *  2. INTEGER q
 */
void splitAt(const char* str, int n, char* left, char* right) {
    int i = 0;
    for (i = 0; i < n && str[i] != '\0'; i++) {
        left[i] = str[i];
    }
    left[i] = '\0';
    
    int j = 0;
    while(str[n] != '\0') {
        right[j++] = str[n++];
    }
    right[j] = '\0';
}

void kaprekarNumbers(int p, int q) {
    int find = 0;
    
    for (int n = p; n <= q; n++) {
        long long sq = (long long)n * n;
        
        char buf[25];
        sprintf(buf, "%lld", sq);
        
        int len = strlen(buf);
        int d = 1;
        int temp = n;
        while(temp >= 10) {
            d++;
            temp /= 10;
        }
        
        int split = len - d;
        if (split < 0) split = 0;
        
        char leftStr[25] = {0};
        char rightStr[25] = {0};
        splitAt(buf, split, leftStr, rightStr);
        
        int left = 0;
        if (strlen(leftStr) > 0) left = strtol(leftStr, NULL, 10);
        
        int right = strtol(rightStr, NULL, 10);
        
        if (left + right == n) {
            printf("%d ", n);
            find++;
        }
    }
    
    if(!find) {
        printf("INVALID RANGE");
    }
}
```

**Go Solution:**
```go
func kaprekarNumbers(p int32, q int32) {
    res := []int{}
    
    for n := int(p); n <= int(q); n++ {
        var sq int64 = int64(n) * int64(n)
        s := strconv.FormatInt(sq, 10);
        
        d := len(strconv.Itoa(n));
        
        rightStr := s[len(s)-d:]
        leftStr := "0"
        if len(s)-d > 0 {
            leftStr = s[:len(s)-d]
        }
        
        left, _ := strconv.Atoi(leftStr)
        right, _ := strconv.Atoi(rightStr)

        if left+right == n {
            res = append(res, n)
        }
    }
    
    if len(res) <= 0 {
        fmt.Println("INVALID RANGE")
        return
    }
    
    for _, v := range res {
        fmt.Printf("%d ", v);
    }
}
```
