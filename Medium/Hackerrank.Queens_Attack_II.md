---
Category: Array
Subcategory: Matrix
Title: Hackerrank. Queens Attack II
Date: 2025-09-15
Difficulty: Medium
Tag: Math, Hash
Status: Accepted
---

### [Hackerrank. Queens Attack II]

[Hackerrank. Queens Attack II]: https://www.hackerrank.com/challenges/queens-attack-2/problem

這題就是在一個西洋棋盤上面，給定一個皇后的位置，然後給定一些障礙物的位置，問這個皇后可以攻擊到多少個位置。

---

### Simulation

最簡單的方法就是去模擬皇后可以攻擊到的所有位置，然後檢查這些位置是否有障礙物，
就可以計算出皇后可以攻擊到多少個位置。

Time Complexity O(N), Space Complexity O(1).

**Golang Solution:**
```go
/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

var directions = [][]int {
    {0, 1}, {1, 0}, {-1, 0}, {0, -1},
    {1, 1}, {1, -1}, {-1, -1}, {-1, 1},
}

func queensAttack(n int32, k int32, r_q int32, c_q int32, obstacles [][]int32) int32 {
    hash := map[string]bool{}
    
    for _, o := range obstacles {
        key := fmt.Sprintf("%d,%d", o[0], o[1])
        hash[key] = true
    }
    
    var res int32 = 0
    
    for d := 0; d < 8; d++ {
        r_a, c_a := directions[d][0], directions[d][1]
        r_que, c_que := int(r_q), int(c_q)
        for true {
            r_que += r_a
            c_que += c_a
            
            if !(r_que > 0 && r_que <= int(n)) {
                break
            }
            
            if !(c_que > 0 && c_que <= int(n)) {
                break
            }
            
            key := fmt.Sprintf("%d,%d", r_que, c_que)
            if hash[key] {
                break
            }
            res++
        }
    }
    return res;
}
```
