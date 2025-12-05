---
Category: String
Subcategory: String
Title: Hackerrank. The Time in Words
Date: 2025-12-05
Difficulty: Medium
Status: Accepted
---

### [Hackerrank. The Time in Words]

[Hackerrank. The Time in Words]: https://www.hackerrank.com/challenges/the-time-in-words/problem

很簡單的題目，給你一個時間的時跟分，然後要你把這個時間用英文的方式說出來。
主要是麻煩在於要把數字轉成英文單字，然後還有一些特殊的時間說法需要特別處理。

---

**Golang Solution**
```go
/*
 * Complete the 'timeInWords' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. INTEGER h
 *  2. INTEGER m
 */
var numToWord = map[int32]string{
    1:  "one",
    2:  "two",
    3:  "three",
    4:  "four",
    5:  "five",
    6:  "six",
    7:  "seven",
    8:  "eight",
    9:  "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "quarter",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    21: "twenty one",
    22: "twenty two",
    23: "twenty three",
    24: "twenty four",
    25: "twenty five",
    26: "twenty six",
    27: "twenty seven",
    28: "twenty eight",
    29: "twenty nine",
    30: "half",
}

func timeInWords(h int32, m int32) string {
    if m == 0 {
        return fmt.Sprintf("%s o' clock", numToWord[h])
    }

    next := (h % 12) + 1

    switch m {
    case 15:
        return fmt.Sprintf("quarter past %s", numToWord[h])
    case 30:
        return fmt.Sprintf("half past %s", numToWord[h])
    case 45:
        return fmt.Sprintf("quarter to %s", numToWord[next])
    }

    if m < 30 {
        if m == 1 {
            return fmt.Sprintf("one minute past %s", numToWord[h])
        }
        return fmt.Sprintf("%s minutes past %s", numToWord[m], numToWord[h])
    }

    remain := 60 - m
    if remain == 1 {
        return fmt.Sprintf("one minute to %s", numToWord[next])
    }
    return fmt.Sprintf("%s minutes to %s", numToWord[remain], numToWord[next])
}
```

**C Solution:**
```c
char* timeInWords(int h, int m) {
    const char* word[] = {
        NULL,
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "quarter",
        "sixteen",
        "seventeen",
        "eightteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
        "half"
    };
    
    char* res = malloc(100);
    
    if (m == 0) {
        sprintf(res, "%s o' clock", word[h]);
        return res;
    }
    
    int next = (h%12) + 1;

    if (m == 15) {
        sprintf(res, "quarter past %s", word[h]);
        return res;
    }
    if (m == 30) {
        sprintf(res, "half past %s", word[h]);
        return res;
    }
    if (m == 45) {
        sprintf(res, "quarter to %s", word[next]);
        return res;
    }

    if (m < 30) {
        if (m == 1) {
            sprintf(res, "one minute past %s", word[h]);
        } else {
            sprintf(res, "%s minutes past %s", word[m], word[h]);
        }
        return res;
    }

    int remain = 60 - m;
    
    if (remain == 1) {
        sprintf(res, "one minute to %s", word[next]);
    } else {
        sprintf(res, "%s minutes to %s", word[remain], word[next]);
    }

    return res;
}
```