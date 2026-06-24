# 2. Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains a single digit.

Add the two numbers and return the sum as a linked list.

### Example

Input:
l1 = [2,4,3]
l2 = [5,6,4]

Output:
[7,0,8]

Explanation:
342 + 465 = 807

---

## Solution Approach

1. Create a dummy node to build the result linked list.
2. Use a pointer (`curr`) to keep track of the current position.
3. Maintain a `carry` value for sums greater than 9.
4. Traverse both linked lists simultaneously.
5. Add corresponding digits along with the carry.
6. Create a new node with `sum % 10`.
7. Update carry using `sum // 10`.
8. Continue until both lists and carry are exhausted.
9. Return `dummy.next`.

---

## Python Solution

---

## Complexity Analysis

### Time Complexity
**O(max(N, M))**

- N = Length of first linked list
- M = Length of second linked list

We traverse each node exactly once.

### Space Complexity
**O(max(N, M))**

The result linked list stores up to max(N, M) + 1 nodes.

---

## LeetCode Submission Stats

| Metric | Result |
|----------|----------|
| Status | ✅ Accepted |
| Test Cases Passed | 1569 / 1569 |
| Runtime | **8 ms** |
| Runtime Ranking | **Beats 52.8%** |
| Memory Usage | **12.5 MB** |
| Memory Ranking | **Beats 21.2%** |

---

## Key Concepts Learned

- Linked Lists
- Dummy Nodes
- Carry Handling
- Iterative Traversal
- Space & Time Complexity Analysis

---

### LeetCode Problem
**#2 - Add Two Numbers**
