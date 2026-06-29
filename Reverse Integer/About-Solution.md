# 🚀 LeetCode 7 - Reverse Integer

![LeetCode](https://img.shields.io/badge/LeetCode-7-orange)
![Language](https://img.shields.io/badge/Language-C%2B%2B-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📝 Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

> Assume the environment does not allow storing 64-bit integers.

---

## 💡 Approach

This solution reverses the integer digit by digit.

### Steps

1. Extract the last digit using `% 10`.
2. Remove the last digit using `/ 10`.
3. Before adding the digit to the reversed number, check whether it will overflow the 32-bit signed integer range.
4. If overflow occurs, return `0`.
5. Otherwise, append the digit to the reversed number.
6. Continue until the original number becomes `0`.

---

## 📊 Complexity Analysis

| Metric | Complexity |
|---------|------------|
| **Time Complexity** | **O(log₁₀ |x|)** |
| **Space Complexity** | **O(1)** |

### Explanation

- The loop runs once for every digit in the integer.
- A number with `d` digits requires `d` iterations.
- Since the number of digits is `log₁₀(|x|)`, the time complexity is **O(log |x|)**.
- Only a few integer variables are used, so the space complexity is **O(1)**.

---

## ⚡ LeetCode Performance

| Metric | Result |
|---------|---------|
| **Status** | ✅ Accepted |
| **Test Cases Passed** | **1045 / 1045** |
| **Runtime** | **3 ms** |
| **Runtime Beats** | **29.4%** |
| **Memory Usage** | **8.5 MB** |
| **Memory Beats** | **83.6%** |
| **Time Complexity (LeetCode)** | **O(log |x|)** |
| **Suggested Complexity** | **O(log |x|)** |

---

## 🎯 Key Concepts

- Integer Manipulation
- Modulo Operator (`%`)
- Division (`/`)
- Overflow Detection
- Simulation

---

## 🧠 What I Learned

- How to reverse an integer without using strings.
- How to safely detect 32-bit integer overflow.
- Using modulo and division together for digit extraction.
- Implementing an optimal **O(log |x|)** solution.

---

## 📌 Tags

`Math` `Integer` `Simulation` `Overflow` `C++`

---

⭐ If you found this repository helpful, consider giving it a **Star**!
