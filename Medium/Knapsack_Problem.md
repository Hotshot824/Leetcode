### Knapsack Problem

在這邊先介紹背包問題(Knapsack Problem) 的基本概念，對於 Knapsack problem 有很多種類型如:
-   **0/1 Knapsack Problem(0/1 背包問題)**
-   **Unbounded Knapsack Problem(無界背包, 完全背包問題)**
-   Multiple Knapsack Problem(多重背包問題)
-   Group Knapsack Problem(分組背包問題)

這邊最主要會針對 0/1 Knapsack Problem 以及 Unbounded Knapsack Problem 來分析，這是最基本會在面試中出現的問題。

![](https://camo.githubusercontent.com/5c7eccec59b5408b776a790f11a8c1f3f0e35948eaac40d95ae45b9c36328df2/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303131373137313330373430372e706e67)

#### 0/1 Knapsack Problem

0/1 Knapsack Problem 是背包問題中最基本的問題，問題描述如下:
1.  有一個背包，最大容量為 `W`
2.  有 `n` 個物品，每個物品的重量為 `w[i]`，價值為 `v[i]`，每個物品只有一個
3.  將那些物品放入背包中，使得背包中物品的總重量不超過 `W`，並且背包中物品的總價值 `V` 最大

0/1 Knapsack Problem 是一個 NP-hard 問題，如果使用回朔法來解決，時間複雜度會是 O(2<sup>n</sup>)，這裡的 `n` 是物品的數量。因此，我們需要使用動態規劃來解決這個問題。

---

**Example:**  
假如這裡有一個背包最大容量為 4，有 3 個物品，每個物品的重量和價值如下:
| item | weight | value |
|:---:| :---:  | :---: |
|  0  |    1   |  15   |
|  1  |    3   |  20   |
|  2  |    4   |  30   |

這個背包能背的最大價值為多少?

這裡使用 Dynamic programming 5 steps 來做分析:

1.  Define the DP array 
    -   這裡使用一種 2D array 的方式來紀錄 DP table
    -   **dp[i][j]** 所代表的是從 i 的物品中選擇，放入容量為 j 的背包中，價值總和最大為多少。這個 2D array 將會如下:
        -   `i` 代表的是物品的數量
        -   `j` 代表的是背包的容量

    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | - | - | - | - | - |
    | 1 | - | - | - | - | - |
    | 2 | - | - | - | - | - |

2.  Determine the recurrence formula
    -   因為 dp[i][j] 的含意，這裡可以有兩個方向推出 dp[i][j]
        -   不放物品 `i`: 由 dp[i-1][j]，這個就是不放當前物品 i 的最大價值
        -   放物品 `i`: 由 dp[i-1][j-w[i]] + v[i] 可以推出當背包容量夠大但是沒有放入物品 i 的最大價值，再加上物品 i 的價值 v[i]，這樣就可以得到放入物品 i 的最大價值
    -   因此可以得到遞推公式: `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])`

3.  Initialize the DP array
    -   先從 dp[i][j] 的定義來看如何初始化，在 dp[i][0] 也就是背包容量為 0 的情況下，不管有多少物品都不可能放入背包，所以 j = 0 都初始化為 0

    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | 0 | - | - | - | - |
    | 1 | 0 | - | - | - | - |
    | 2 | 0 | - | - | - | - |

    -   初始化 dp[0][j] 的情況，dp[0][j] 所代表的是這個 0/1 item 中可以選擇的 minimum weight item，因此只要當 j >= w[0]，的時候就可以放入物品 0
    -   因此這個初始化的情況可以得到以下代碼:

    ```go
    /*
    w is a array of weight, W is the maximum capacity of the knapsack.
    j := w[0] means item 0 can be put into the backpack.
    */
    for j := w[0]; j <= W; j++ {
        dp[0][j] = value[0]
    }
    ```

    -  這樣我們就可以得到以下的 DP table:

    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | 0 | 15 | 15 | 15 | 15 |
    | 1 | 0 | - | - | - | - |
    | 2 | 0 | - | - | - | - |

4.  Determine the traversal order
    -   這裡要討論的是應該要先遍歷物品 i 還是先遍歷背包的容量 j，在這個題目中兩個都是可以的
    -   注意到 dp[i][j] 是依照 dp[i-1][j] 和 dp[i-1][j-w[i]] 來推導出來的，所以無論是 j 或是 i 都可以先遍歷出之前的結果

先走 i 就是從左往右，每次都先算完 i 的最大價值
![](https://camo.githubusercontent.com/e65a808fdca1dd85e9136fa876a1dcbfafcfa0ac3ab555608f7eef48976348c6/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f3230323130313130313033323132342e706e67)

先走 j 就是從上往下，每次都先算完 j 的最大價值
![](https://camo.githubusercontent.com/7c3f1416e512489dae82a951b6d4a83e35562def59ba1661da408035073b1653/68747470733a2f2f636f64652d7468696e6b696e672d313235333835353039332e66696c652e6d7971636c6f75642e636f6d2f706963732f32303231303131303130333234343730312e706e67)

5.  Example to derive dp array
    -   最後推導出的 DP table 如下:

    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | 0 | 15 | 15 | 15 | 15 |
    | 1 | 0 | 15 | 15 | 20 | 35 |
    | 2 | 0 | 15 | 15 | 20 | 35 |

    -   最後的結果就是 dp[2][4] = 35
    -   要注意這個結果所代表的是在這些 item 的選擇下，以 4 為容量的背包所能達到的最大價值

實現這個 0/1 Knapsack Problem 的代碼如下:
```go
func knapsack_2D(weight, value []int, W int) int {
    dp := make([][]int, len(weight))
    for i, _ := range dp {
        dp[i] = make([]int, W + 1)
    }

    // initialization the dp table
    for j := weight[0]; j <= W; j++ {
        dp[0][j] = value[0]
    }

    for i := 1; i < len(weight); i++ {
        for j := 0; j <= W; j++ {
            // if the knapsack's capacity is not enough to put the item i
            if (j < weight[i]) {
                dp[i][j] = dp[i-1][j];
            } else {
                dp[i][j] = maxInt(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
            }
        }
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
	weight := []int{1,3,4}
	value := []int{15,20,30}
	knapsack_2D(weight,value,4)
}
```

---

### 0/1 Knapsack Problem Scrolling Array

上面是用一個 2D array 的方式來解決 0/1 Knapsack problem，但是我們還可以更進一步的優化這個解法使用一個 1D array(Scrolling array) 來解決這個問題。

還是相同的例子:

假如這裡有一個背包最大容量為 4，有 3 個物品，每個物品的重量和價值如下:
| item | weight | value |
|:---:| :---:  | :---: |
|  0  |    1   |  15   |
|  1  |    3   |  20   |
|  2  |    4   |  30   |

這個背包能背的最大價值為多少?

使用 2D array 的時候遞推公式是 `dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])`，其實可以把 dp[i-1] 的結果覆蓋到 dp[i] 上，
這樣的話表達式就會變成 `dp[j] = max(dp[j], dp[j-w[i]] + v[i])`，這樣就可以用一個 1D array 來解決這個問題。

Dynamic programming 5 steps:
1.  Define the DP array
    -   在一個 1D array 中，`dp[j]` 代表的是背包容量為 j 的情況下，所能達到的最大價值
2.  Determine the recurrence formula
    -   放物品的最大價值: `dp[j-w[i]] + v[i]`
        -   `dp[j-w[i]]` 代表的是背包容量為 j-w[i] 的情況下，所能達到的最大價值，再加上物品 i 的價值 v[i]
    -   因此可以得到遞推公式: `dp[j] = max(dp[j], dp[j-w[i]] + v[i])`
3.  Initialize the DP array
    -   這裡初始化的情況和上面一樣，但是注意遞推公式的 `dp[j] = max(dp[j], dp[j-w[i]] + v[i])`，無論如何都會取 max，所以初始化的情況可以把全部初始化為 0
4.  Determine the traversal order
    -   這裡要注意順序跟 2D array 是不一樣的，必須以從大到小的順序來遍歷，這是為了避免物品被重複放入背包中，例如 i == 0 的時候:
        -   在 dp[1] 的時候 `dp[1] = dp[1 - weight[0]] + value[0] = 15`
        -   在 dp[2] 的時候 `dp[2] = dp[2 - weight[0]] + value[0] = 30`
        -   這樣 i 就會被重複放入背包中，更新 dp[2] 的時候 dp[1] 的值已經被更新過了
    -   而如果是從大到小的順序的話，就不會有這個問題:
        -   在 dp[2] 的時候 `dp[2] = dp[2 - weight[0]] + value[0] = 15`
        -   在 dp[1] 的時候 `dp[1] = dp[1 - weight[0]] + value[0] = 15`
        -   這樣就不會有重複放入背包的問題，更新順序變成 dp[2] -> dp[1] -> dp[0]
5.  Example to derive dp array
    -   我們使用 1D array 依序物品 0, 1, 2 來更新 DP array，最後的結果如下:

    | i/j | 0 | 1 | 2 | 3 | 4 |
    |:---:| :---: | :---: | :---: | :---: | :---: |
    | 0 | 0 | 15 | 15 | 15 | 15 |
    | 1 | 0 | 15 | 15 | 20 | 35 |
    | 2 | 0 | 15 | 15 | 20 | 35 |

實現的相關代碼如下:
```go
func knapsack_1D(weight, value []int, W int) int {
	dp := make([]int, W+1)
	// Items iteration order
	for i := 0; i < len(weight); i++ {
		// Reverse order to avoid duplicate items
		for j := W; j >= weight[i]; j-- {
			// Update the dp array
			dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
		}
	}
	return dp[W]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	weight := []int{1, 3, 4}
	value := []int{15, 20, 30}
	knapsack_1D(weight, value, 4)
}
```