# 1. Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you may not use the same element twice.

### Example

```text
Input: nums = [2,7,11,15]
Target: 9

Output: [0,1]
```

Explanation:

```text
nums[0] + nums[1] = 2 + 7 = 9
```

---

## Approach

This solution uses the **Brute Force** approach.

The idea is:

1. Pick one number from the array.
2. Compare it with every number after it.
3. Check if their sum equals the target.
4. If the target is found, store the indices and return the answer.

Since every possible pair is checked, the solution is guaranteed to find the correct answer.

---

## Intuition

For every element in the array, we try pairing it with the remaining elements.

For example:

```text
nums = [2,7,11,15]
target = 9
```

Possible pairs:

```text
2 + 7
2 + 11
2 + 15
7 + 11
7 + 15
11 + 15
```

The first pair gives:

```text
2 + 7 = 9
```

Therefore, the answer is:

```text
[0,1]
```

---

## Dry Run

### Input

```python
nums = [2,7,11,15]
target = 9
```

### Iteration 1

```python
i = 0
nums[i] = 2
```

Inner loop:

```python
j = 1
nums[j] = 7
```

Check:

```python
2 + 7 = 9
```

Condition becomes true.

Store indices:

```python
[0,1]
```

Return answer.

---

## Python Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        it = 1
        result = []

        for i in range(len(nums)):
            for j in range(it, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    break

            it += 1

            if len(result) != 0:
                break

        return result
```

---

## How the Code Works

### Step 1

Create a variable to control the starting position of the second loop.

```python
it = 1
```

Create an empty list to store the answer.

```python
result = []
```

### Step 2

Loop through the array.

```python
for i in range(len(nums)):
```

### Step 3

Start checking all elements after the current index.

```python
for j in range(it, len(nums)):
```

### Step 4

Check whether the current pair equals the target.

```python
if nums[i] + nums[j] == target:
```

### Step 5

Store the indices.

```python
result.append(i)
result.append(j)
```

### Step 6

Break out of the loops once the answer is found.

```python
break
```

### Step 7

Return the result.

```python
return result
```

---

## Complexity Analysis

### Time Complexity

```text
O(n²)
```

Reason:

- Two nested loops are used.
- In the worst case, every possible pair must be checked.

### Space Complexity

```text
O(1)
```

Reason:

- Only a few extra variables are used.
- The result contains at most two indices.

---

## What I Learned

- Using nested loops to check all possible pairs.
- Traversing arrays using indices.
- Using conditions to find a required pair.
- Using `break` to stop unnecessary iterations.
- Understanding the Brute Force approach.

---

## Tags

- Array
- Hash Table
- Brute Force
- LeetCode Easy
- Python
