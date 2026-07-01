# 1189. Maximum Number of Balloons

**Difficulty:** Easy
**Topics:** Hash Table, String, Counting

## Problem

Given a string `text`, you want to use the characters of `text` to form as many instances of the word `"balloon"` as possible.

You can use each character in `text` at most once. Return the maximum number of instances of `"balloon"` that can be formed.

**Example:**
```
Input:  text = "nlaebolko"
Output: 1
```
```
Input:  text = "loonbalxballpoon"
Output: 2
```
```
Input:  text = "leetcode"
Output: 0
```

## Intuition

Think of it like a craft project: you have a bunch of loose letter tiles (`text`), and you're trying to spell out the word `"balloon"` as many times as you can, using each tile only once.

Spell out `"balloon"` letter by letter:

```
b - a - l - l - o - o - n
```

Notice something important: `l` shows up **twice** and `o` shows up **twice**. Every other letter (`b`, `a`, `n`) shows up **once**.

So to build **one** `"balloon"`, you need:
- 1 `b`
- 1 `a`
- 2 `l`s
- 2 `o`s
- 1 `n`

To build **k** copies of `"balloon"`, you'd need `k` of each single letter, and `2k` of each doubled letter.

This means the number of complete `"balloon"`s you can build is limited by whichever letter runs out first — the "bottleneck" letter. That's the key insight: **the answer is a minimum over all the letters, each scaled by how many times it's needed per word.**

## Step-by-Step Approach

**Step 1 — Count every letter in `text`.**
Walk through the string once and build a frequency table (a dictionary/hash map) mapping each character to how many times it appears.

**Step 2 — Figure out how many "balloon"s each letter alone could support.**
For each of the 5 relevant letters, ask: "if this were the *only* letter I cared about, how many balloons could I make?"
- `count['b']` → each word eats 1 `b`, so this count directly tells you the max words supportable.
- `count['a']` → same logic, 1 `a` per word.
- `count['n']` → same logic, 1 `n` per word.
- `count['l'] // 2` → each word eats 2 `l`s, so divide by 2 (integer division, since you can't use half an `l`).
- `count['o'] // 2` → same logic, divide by 2.

**Step 3 — Take the minimum.**
Since every single word requires *all five* letters at once, you're limited by whichever letter supports the fewest words. Taking the `min()` of the five values gives the true maximum number of complete `"balloon"`s you can assemble.

**Step 4 — Handle missing letters.**
If a letter never appears in `text` at all, treat its count as `0` (using `.get(char, 0)` instead of indexing directly avoids a `KeyError` and correctly makes the answer `0` in that case).

---

## Walkthrough Example

For `text = "loonbalxballpoon"`, spelling out each character:

```
l-o-o-n-b-a-l-x-b-a-l-l-p-o-o-n
```

1. Count letters: `{'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2, 'x': 1, 'p': 1}`
2. Compute per-letter word capacity:
   - `b` → 2
   - `a` → 2
   - `l` → 4 // 2 = 2
   - `o` → 4 // 2 = 2
   - `n` → 2
3. Take the minimum: `min(2, 2, 2, 2, 2) = 2`

Every letter supports exactly 2 words here, so nothing is a bottleneck and the answer is **2** — matching the expected output. In a case where, say, `b` only appeared once, `min()` would catch that and cap the answer at 1, even if every other letter had plenty of supply left over.

## Complexity

- **Time Complexity:** O(N), where N is the length of `text`. The algorithm makes a single pass through the string to build the frequency table; everything after that is a fixed number of dictionary lookups and a `min()` over 5 values (constant time).
- **Space Complexity:** O(1). Even though we use a dictionary, it can hold at most 26 keys (one per lowercase English letter), so its size doesn't grow with the input — it's bounded by a constant.

## Why This Is Optimal

You can't do better than O(N) time here because you must at least *look at* every character in `text` once to know what you're working with — there's no way to skip characters and still guarantee correctness. And since the extra space is capped at 26 entries no matter how large `text` gets, O(1) space is as good as it gets too. This is confirmed by LeetCode's own suggested complexity of O(N), matching the submitted solution exactly.

## Results

| Metric | Value | Percentile |
|--------|-------|------------|
| Runtime | 3 ms | Beats 56.9% |
| Memory | 19.2 MB | Beats 74.5% |

**Status:** ✅ Accepted — 28/28 testcases passed
