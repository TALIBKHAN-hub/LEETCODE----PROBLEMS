# 3. Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

### Example 1

```text
Input: s = "abcabcbb"
Output: 3

Explanation:
The answer is "abc", with length 3.
```

### Example 2

```text
Input: s = "bbbbb"
Output: 1

Explanation:
The answer is "b", with length 1.
```

### Example 3

```text
Input: s = "pwwkew"
Output: 3

Explanation:
The answer is "wke", with length 3.
```

---

## Approach

This solution uses the **Sliding Window** technique along with a **Hash Set**.

- `l` represents the left pointer of the window.
- `r` represents the right pointer of the window.
- `seen` stores the characters currently inside the window.
- If a duplicate character is found, move the left pointer forward and remove characters from the set until the duplicate is removed.
- Update the maximum window size during each iteration.

---

## Dry Run

### Input

```text
s = "abcabcbb"
```

### Steps

| Right Pointer | Character | Window | Longest |
|--------------|-----------|---------|----------|
| 0 | a | a | 1 |
| 1 | b | ab | 2 |
| 2 | c | abc | 3 |
| 3 | a | bca | 3 |
| 4 | b | cab | 3 |
| 5 | c | abc | 3 |
| 6 | b | cb | 3 |
| 7 | b | b | 3 |

### Result

```text
Output = 3
```

---

## Complexity Analysis

### Time Complexity

```text
O(n)
```

Each character is added to and removed from the set at most once.

### Space Complexity

```text
O(min(n, m))
```

Where:

- `n` = length of the string
- `m` = number of unique characters

The set stores only unique characters in the current window.

---

## Key Concepts Used

- Sliding Window
- Two Pointers
- Hash Set
- String Manipulation

---

## LeetCode Link

🔗 https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

### Author

**Talib Alam**
