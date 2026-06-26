# 4. Median of Two Sorted Arrays

## 📝 Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the **median** of the two sorted arrays.

The overall run time complexity should ideally be **O(log(m+n))**.

---

## 💡 My Approach

1. Merge both arrays into a single list.
2. Sort the merged list.
3. Check whether the total number of elements is odd or even.
4. If the length is odd:
   - Return the middle element.
5. If the length is even:
   - Find the two middle elements.
   - Return their average.

---

## ⏱️ Time Complexity

- Merging the arrays: **O(m + n)**
- Sorting the merged array: **O((m + n) log(m + n))**
- Finding the median: **O(1)**

**Overall Time Complexity:**

```
O((m + n) log(m + n))
```

---

## 💾 Space Complexity

The merged array stores all elements from both arrays.

**Space Complexity:**

```
O(m + n)
```

---

## 📊 LeetCode Performance

> Replace these values with your actual submission results.

- **Runtime:** XX ms
- **Memory Usage:** XX MB

---

## 📚 What I Learned

- How to merge multiple arrays.
- How Python's `sort()` function works.
- Finding the median for both odd and even length arrays.
- Time and space complexity analysis.

---

## ⚠️ Note

Although this solution is simple and easy to understand, it **does not meet** the required **O(log(m+n))** time complexity mentioned in the problem statement because it sorts the merged array.

The optimal solution uses **Binary Search** and achieves:

- **Time Complexity:** `O(log(min(m, n)))`
- **Space Complexity:** `O(1)`

This implementation is intended as a beginner-friendly solution.
