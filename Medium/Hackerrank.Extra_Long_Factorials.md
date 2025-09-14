---
Category: Math
Subcategory: Math
Title: Hackerrank. Extra Long Factorials
Date: 2025-09-13
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Extra Long Factorials]

[Hackerrank. Extra Long Factorials]: https://www.hackerrank.com/challenges/extra-long-factorials/problem

這題本意其實是叫你做 Big Number Multiplication，因為即使是 Unsigned 64-bit Integer 也無法存下 30! 的結果。

> Unsigned 64-bit Integer 的最大值是 2^64 - 1 = 18,446,744,073,709,551,615，最多只能存到 20!。

---

### Golang Math/Bignum

先偷吃步，Golang 本身就有支援 Big Number 的套件 math/big，所以直接用就好。
實作上也不會要求你自己實作 Big Number Multiplication，如果要用 CPP 就必須實作直式乘法。

**Golang Solution:**
```go
/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

func extraLongFactorials(n int32) {
    result := big.NewInt(1)
    base := big.NewInt(int64(n))
    one := big.NewInt(1)
    zero := big.NewInt(0)

    for base.Cmp(zero) > 0 {
        result.Mul(result, base)
        base.Sub(base, one)
    }

    fmt.Println(result)
}
```

---

### Big Number Multiplication

實作大數乘法，這邊用字串來存放大數，然後模擬直式乘法的過程。

1. 先檢查如果其中一個數是 0，直接回傳 "0"
2. 將兩個字串反轉，並轉成數字陣列
    -   反轉是為了方便在 For loop 中從 0 index 往後處理
3. 建立一個結果陣列，長度是 m + n (乘法結果的最大長度)
4. 兩層 For loop，模擬直式乘法
    -   將 num1[i] * num2[j] 的結果加到 result[i+j] 上
    -   若 result[i+j] >= 10，進位到 result[i+j+1]
5. 找出結果陣列的最高位數，去除 m+n 長度中沒有用到的位子

Time Complexity: O(n^2), Space Complexity: O(n).

**Golang Solution:**
```go
/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

func extraLongFactorials(n int32) {
    result := "1"

    for n > 0 {
        result = bigNumberMul(result, strconv.Itoa(int(n)))
        n--
    }
    
    fmt.Println(result)
}

func bigNumberMul(a, b string) string {
    if a == "0" || b == "0" {
        return "0"
    }
    
    m, n := len(a), len(b)
    num1 := make([]int, m)
    num2 := make([]int, n)
    for i := 0; i < m; i++ {
        num1[m-1-i] = int(a[i] - '0')
    }
    for i := 0; i < n; i++ {
        num2[n-1-i] = int(b[i] - '0')
    }
    
    result := make([]int, m+n)
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            result[i+j] += num1[i] * num2[j]
            if result[i+j] >= 10 {
                result[i+j+1] += result[i+j] / 10
                result[i+j] %= 10
            }
        }
    }
    
    idx := m + n - 1
    for idx > 0 && result[idx] == 0 {
        idx--
    }
    
    var sb strings.Builder
    for i := idx; i >= 0; i-- {
        sb.WriteByte(byte(result[i] + '0'))
    }
    
    return sb.String()
}
```

**CPP Solution:**
```cpp
/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */

string bigNumberMul(string a, string b) {
    if (a == "0" || b == "0") {
        return "0";
    }
    
    int m = a.size(), n = b.size();
    vector<int> num1(m, 0);
    vector<int> num2(n, 0);
    for (int i = m - 1; i >= 0; i--) {
        num1[m - 1 - i] = (int)a[i] - '0';
    }
    for (int i = n - 1; i >= 0; i--) {
        num2[n - 1 - i] = (int)b[i] - '0';
    }
    
    vector<int> result(m+n, 0);
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            result[i+j] += num1[i] * num2[j];
            if (result[i+j] >= 10) {
                result[i+j+1] += result[i+j] / 10;
                result[i+j] %= 10;
            }
        }
    }
    
    int idx = m + n - 1;
    while (idx > 0 && result[idx] == 0) {
        idx--;
    }

    string ans;
    for (int i = idx; i >= 0; i--) {
        ans.push_back(result[i] + '0');
    }
    
    return ans;
}


void extraLongFactorials(int n) {
    string result = "1";
    
    while (n > 0) {
        result = bigNumberMul(result, to_string(n));
        n--;
    }
    
    std::cout << result << std::endl;
}
```