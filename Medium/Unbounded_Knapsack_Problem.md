---
Category: Dynamic Programming
Subcategory: Unbounded Knapsack Problem
Title: Unbounded Knapsack Problem
Date: 2025-09-12
Difficulty: Medium
Status: Accepted
---
### Unbounded Knapsack Problem

Unbounded Knapsack Problem 是背包問題中的另一個問題，把 0/1 的物品數量改成一個物品可以選擇無限次數，問題描述如下:

1. 有一個背包，最大容量為 `4`
2. 有 3 個物品，每個物品的重量和價值如下:

| item | weight | value |
|:---:|:---:|:---:|
| 0 | 1 | 15 |
| 1 | 3 | 50 |
| 2 | 4 | 70 |

這裡我們可以回頭去看 0/1 Knapsack Problem 的解法，以下是 0/1 Knapsack 的核心程式碼:

```c
for(int i = 0; i < weight.size(); i++) { // Traversal items
    for(int j = bagWeight; j >= weight[i]; j--) { // Traversal bag weight
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
}
```

-   在 0/1 Knapsack 關於 weight 的歷遍是從大到小，這是因為我們要確保每個物品只能選擇一次
    -   所以反過來說在 Unbounded Knapsack 關於 weight 的歷遍是從小到大，這是因為我們可以選擇無限次數
    -   關於這裡的詳細解釋可以參考 [Knapsack Problem] 中為什麼要從大到小歷遍
-   所以把 0/1 Knapsack 的程式碼改成 Unbounded Knapsack 的程式碼如下:

```c
for(int i = 0; i < weight.size(); i++) { // Traversal items
    for(int j = weight[i]; j <= bagWeight; j++) { // Traversal bag weight
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);
    }
}
```

---

-   回到這個例子，假如我們以 2D 的方式來解掉這題的話，會得到以下的結果:
    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | 0 | 15 | 30 | 45 | 60 |
    | 1 | 0 | 15 | 30 | **50** | 65 |
    | 2 | 0 | 15 | 30 | 50 | **70** |

-   這個例子特意設計成物品會在同等重量下，選擇重量大的物品價值會比較高
    -   因此在 j = 3, 4 的時候會選擇物品 1 和 2
-   在 2D array 的解法中，變成必須比較兩層物品的價值，因為物品是可以重複放入所自己這層也要比較

Example solution:
```go
func unbounded_knapsack_2D(weight, value []int, W int) int {
	dp := make([][]int, len(weight))
	for i := range dp {
		dp[i] = make([]int, W+1)
	}

	// initialization the dp table
	for j := weight[0]; j <= W; j++ {
		dp[0][j] = maxInt(dp[0][j], dp[0][j-weight[0]]+value[0])
	}

	for i := 1; i < len(weight); i++ {
		for j := 0; j <= W; j++ {
			// if the knapsack's capacity is not enough to put the item i
			if j < weight[i] {
				dp[i][j] = dp[i-1][j]
			} else {
                // Compare 2 times: 
                // 1. Compare previous item's value
                // 2. Compare current item's value
                dp[i][j] = maxInt(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
				dp[i][j] = maxInt(dp[i][j], dp[i][j-weight[i]]+value[i])
			}
		}
		fmt.Println(dp)
	}
	return dp[len(weight)-1][W]
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	weight := []int{1, 3, 4}
	value := []int{15, 50, 70}
	unbounded_knapsack_2D(weight, value, 4)
}
```

[Knapsack Problem]: ./Knapsack_Problem.md