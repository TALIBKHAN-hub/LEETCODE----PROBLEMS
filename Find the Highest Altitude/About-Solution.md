# 1732. Find the Highest Altitude

**Difficulty:** Easy
**Topics:** Array, Prefix Sum

## Problem Statement

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the **net gain in altitude** between points `i` and `i + 1` for all `0 <= i < n`. Return *the highest altitude of a point.*

---

### Example 1
```
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
```

---

### Example 2
```
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
```

### Constraints
- `n == gain.length`
- `1 <= n <= 100`
- `-100 <= gain[i] <= 100`

---

### Approach
This solution uses a **prefix sum** technique. Starting at altitude `0`, it iterates through the `gain` array, accumulating the running altitude (`current`) at each step and storing it in a list. The final answer is the maximum value in that list of altitudes.

## Complexity Analysis

| Metric | Current | Suggested |
|---|---|---|
| Time Complexity | O(N) | O(N) |
| Space Complexity | O(N) | O(1) |

---

## Submission Results

- **Status:** ✅ Accepted
- **Test Cases:** 80 / 80 passed
- **Runtime:** 0 ms (Beats 100.0% of submissions)
- **Memory:** 12.3 MB (Beats 89.0% of submissions)

---
*Solved on LeetCode — submission documented for portfolio/GitHub tracking.*
