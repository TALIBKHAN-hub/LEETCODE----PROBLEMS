# 5. Longest Palindromic Substring

## 📝 Problem

Given a string `s`, return the **longest palindromic substring** in `s`.

A palindrome is a string that reads the same forward and backward.

### Example

**Input**
```text
s = "babad"
```

**Output**
```text
"bab"
```

Another valid answer is `"aba"`.

---

## 💡 Approach

This solution uses the **Expand Around Center** technique.

A palindrome can have:

- **Odd length** (center is one character)
- **Even length** (center is between two characters)

For every index in the string:

1. Expand around the current character (odd palindrome).
2. Expand around the current and next character (even palindrome).
3. Compare both results with the current longest palindrome.
4. Return the longest substring found.

This approach avoids checking every possible substring and is much more efficient than the brute-force solution.

---

## ⏱️ Time Complexity

| Operation | Complexity |
|-----------|------------|
| Expand around each center | **O(N²)** |

**Overall Time Complexity:** **O(N²)**

---

## 💾 Space Complexity

**O(1)**

Only a few variables are used, and no extra data structures proportional to the input size are required.

---

## 📊 LeetCode Performance

- ✅ Status: Accepted
- ✅ Test Cases Passed: **143 / 143**
- ⚡ Runtime: **221 ms** *(Beats 88.6% of Python submissions)*
- 💾 Memory Usage: **19.3 MB** *(Beats 69.3% of Python submissions)*

---

## 📚 Key Concepts Learned

- Two Pointers
- Expand Around Center
- String Manipulation
- Palindrome Detection
- Time Complexity Analysis

---

## 🚀 Notes

This solution uses the **Expand Around Center** approach, which is the standard interview solution for this problem.

Although the optimal solution is **Manacher's Algorithm (O(N))**, it is much more complex. For most coding interviews, this approach is preferred because it is simple, readable, and performs efficiently.
