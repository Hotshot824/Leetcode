---
Category: Array
Subcategory: Binary Search
Title: Hackerrank. Climbing the Leaderboard
Date: 2025-09-13
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Climbing the Leaderboard]

[Hackerrank. Climbing the Leaderboard]: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

Hackerrank 的題目，給一個 leaderboard 的分數陣列和一個玩家每次遊戲的分數陣列，
找出玩家每次遊戲後在 leaderboard 上的排名。

這題不用把每次的分數都重新插入 leaderboard，所以只要找當下分數在 leaderboard 上的排名即可。

---

### Binary Search

1. 先把 leaderboard 的分數去重並排序
2. 對於每次玩家的分數，使用 Binary Search 找出該分數在 leaderboard 上的排名

Time Complexity O(N log M), Space Complexity O(N).

**Golang Solution:**
```go
/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */

func climbingLeaderboard(ranked []int32, player []int32) []int32 {
    // Write your code here
    rank := []int32{}
    for i := 0; i < len(ranked); i++ {
        if i+1 < len(ranked) && ranked[i] == ranked[i+1] {
            continue
        }
        rank = append(rank, ranked[i])
    }
    
    res := []int32{}
    
    for _, s := range player {
        res = append(res, binaryInsert(rank, s)+1)
    }
    
    return res
}

func binaryInsert(ranked []int32, score int32) int32 {
    left, right := 0, len(ranked)
    for (left < right) {
        mid := left + (right - left)/2
        
        if (ranked[mid] > score) {
            left = mid + 1;
        } else {
            right = mid
        }
    }
    
    return int32(left)
}
```