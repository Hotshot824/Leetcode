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

### CPP Big Number Multiplication

TBD...