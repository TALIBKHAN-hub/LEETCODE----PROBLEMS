# 9. Palindrome Number

![Accepted](https://img.shields.io/badge/Status-Accepted-brightgreen) ![Language](https://img.shields.io/badge/Language-Python-blue) ![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward.

**Example 1:**
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it reads 121-. Therefore it is not a palindrome.
```

**Example 3:**
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

---

## Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        temp = x
        
        while temp > 0:
            digit = temp % 10
            reverse = reverse * 10 + digit
            temp = temp // 10

        if (x == reverse):
            return True
        else:
            return False
```

---

## Approach & Intuition

1. **Early exit** — Any negative number is immediately rejected since a minus sign can't be mirrored.
2. **Digit reversal** — Instead of converting to a string, we mathematically reverse the integer:
   - Extract the last digit using `% 10`
   - Build the reversed number by shifting left (`* 10`) and appending the digit
   - Remove the last digit from `temp` using `// 10`
3. **Comparison** — If the reversed number equals the original, it's a palindrome.

---

## Complexity Analysis

| | Complexity | Explanation |
|---|---|---|
| **Time** | `O(log X)` | We iterate once per digit; the number of digits in X is `log₁₀(X)` |
| **Space** | `O(1)` | Only a constant number of variables are used |

> ✅ **Perfect efficiency!** This solution already achieves the optimal time and space complexity.

---

## Submission Results

| Metric | Value | Percentile |
|---|---|---|
| **Status** | Accepted | 11511 / 11511 test cases passed |
| **Runtime** | 7 ms | Beats **63.2%** of Python submissions |
| **Memory** | 19.2 MB | Beats **52.9%** of Python submissions |

---

## Why Not String Conversion?

A common alternative is `str(x) == str(x)[::-1]`, but the mathematical approach used here:
- Avoids extra memory allocation for string creation
- Is more aligned with the problem's **follow-up challenge** (solve it without converting to a string)
- Demonstrates a deeper understanding of number manipulation
