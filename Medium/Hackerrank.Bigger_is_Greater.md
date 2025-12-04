---
Category: String
Subcategory: String
Title: Hackerrank. Bigger is Greater
Date: 2025-12-04
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. Bigger is Greater]

[Hackerrank. Bigger is Greater]: https://www.hackerrank.com/challenges/bigger-is-greater/problem

做這題之前可以先用數字來思考怎麼找到下一個最小的更大排列組合。

1. `1234` -> `1243`
    -   對於 `1234` 完全依照遞增排列，所以從右邊開始找，找到第一個 s[i] < s[i+1] 的位置交換
2. `1243` -> `1324`
    -   找到 `2` 才能確定可以跟後方中最小的 `3` 交換
3. `21433` -> `23134`
    -   找到 `1` 才能確定可以跟後方中最小的 `3` 交換
    -   交換後，後方的 `41` 需要反轉成 `14` 才是下一個最小的排列組合
        -   因為第一步的交換使 `1` 取代了後方最小的 `3`
        -   所以後方的數字需要重新排列成最小的排列組合

從上面的例子我們能把找下一個排列的過程總結如下:

1.  從右邊開始找，找到第一個 s[i] < s[i+1] 的位置 i，這是位數最小的可以交換的位置
    -   如果找不到，表示已經是最大的排列組合，回傳 "no answer"
2.  從右邊開始找，找到第一個 s[j] > s[i] 的位置 j
    -   這步驟的目的是從最小位數開始找，找到可以比 s[i] 大的數字來交換
3.  交換 s[i] 和 s[j]，然後把 i 後方的數字反轉成最小的排列組合

```
1. Find i
1234 1243 21433 4321 43251
  ^   ^    ^           ^
2. Find j
1234 1243 21433 ---- 43251
   ^    ^     ^         ^
3. Swap i and j
1243 1342 23431 ---- 43521
  ^^  ^ ^  ^  ^        ^^
4. Reverse from i+1 to end
1243 1324 23134 ---- 43512
```

以上就是完整的算法，接下來只要實作即可。

---

**Golang Solution:**
```go
/*
 * Complete the 'biggerIsGreater' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING w as parameter.
 */
func biggerIsGreater(w string) string {
    arr := []byte(w)

    // Step 1: Find i
    var i int = len(arr)-2
    for i >= 0 && arr[i] >= arr[i+1] {
        i--
    }
    
    if (i < 0) {
        return "no answer"
    }
    
    // Step 2: Find j and swap w[i] and w[j]
    for j := len(arr)-1; j > i; j-- {
        if (arr[j] > arr[i]) {
            arr[i], arr[j] = arr[j], arr[i]
            break
        }
    }
    
    // Step 3: Reverse from i+1 to end
    left, right := i+1, len(arr)-1
    for right > left {
        arr[left], arr[right] = arr[right], arr[left]
        left++
        right--
    }
    
    return string(arr)
}
```

**C Solution:**
```c
char* biggerIsGreater(char* w) {
    int n = strlen(w);
    int i = n - 2;
    
    while(i >= 0 && w[i] >= w[i+1]) {
        i--;
    }
    
    if(i < 0) {
        return "no answer";
    }
    
    for (int j = n-1; j > i; j--) {
        if (w[j] > w[i]) {
            char tmp = w[i];
            w[i] = w[j];
            w[j] = tmp;
            break;
        }
    }
    
    int left = i + 1, right = n - 1;
    while(left < right) {
        char tmp = w[left];
        w[left] = w[right];
        w[right] = tmp;
        left++;
        right--;
    }
    
    return w;
}
```