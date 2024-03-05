### Martix

大部分的 Martix 都是用 array 來表示的，處理的時候要注意觀察 Martix 的變化跟 Array 的特性。

### [48. Rotate Image]

這題特殊的地方在於不能使用額外的空間，所以只能在原本的 Martix 上面做操作，所以一定會有一個 temp 變數來暫存值。

所以先觀察 index 的變化，以 3x3 的 Martix 為例：

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)


[48. Rotate Image]: https://leetcode.com/problems/rotate-image/