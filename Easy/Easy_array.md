### Easy Array

跟 Array 相關的題目，主要是要熟悉 Array 的操作，例如：新增、刪除、修改、查詢等等，到更進階的 two pointer、sliding window 等。
但是 Easy 的題目通常不會太複雜，所以不需要太多的技巧，只要熟悉基本的操作就可以了。

### [2864. Maximum Odd Binary Number]

最大的 Odd Binary 一定是以 1 結尾，所以保留一個 1 剩下的 1 全部排到前面，後面補 0 即可。

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